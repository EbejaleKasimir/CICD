import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pyodbc

def create_database(database_name):
    """Creates a new database in PostgreSQL.

    Args:
        database_name: The name of the database to create.
    """
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(
            user="postgres",
            password="demopass",
            host="localhost",
            port="5432",
            database="postgres"
        )

        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # Create a new cursor
        cur = conn.cursor()

        # Check if the database exists
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{database_name}'")
        exists = cur.fetchone()

        if not exists:
            # Execute the CREATE DATABASE statement
            cur.execute(f"CREATE DATABASE {database_name};")
            print(f"Database {database_name} created successfully.")
        else:
            print(f"Database {database_name} already exists.")

        # Close the cursor and the connection
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error occurred while creating database {database_name}. Error message: {error}")

if __name__ == "__main__":

    # Create database
    database_name = "wpi_data"
    create_database(database_name)

    # Create SQLAlchemy engine
    database_url = "postgresql://postgres:demopass@localhost/wpi_data"
    engine = create_engine(database_url)

    # Read Access data into DataFrame
    current_dir = os.path.dirname(os.path.realpath(__file__))
    cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+current_dir+'/WPI.mdb;') 
    data = pd.read_sql("SELECT * FROM [Wpi Data]", cnxn)

    # Load data into PostgreSQL
    data.to_sql("wpi_data_tbl", engine, if_exists='replace', index=False)

    # Connect to the database
    conn = psycopg2.connect(database="wpi_data", user="postgres", password="demopass")

    # Queries
    create_function_query = """
    CREATE OR REPLACE FUNCTION haversine(
    lat1 float,
    lon1 float,
    lat2 float,
    lon2 float
    ) RETURNS float AS $$
    DECLARE
    x float := 69.1 * (lat2 - lat1);
    y float := 69.1 * (lon2 - lon1) * cos(radians(lat1));
    BEGIN
    RETURN sqrt(x^2 + y^2) * 1.609344;
    END;
    $$ LANGUAGE plpgsql;
    """

    query1 = """
    SELECT
    "Main_port_name" AS port_name,
    haversine(CAST("Latitude_degrees" AS float),
    CAST("Longitude_degrees" AS float),
    CAST(1.0 AS float),
    CAST(1.0 AS float)) AS distance_in_kilometers
    FROM
    wpi_data_tbl
    WHERE
    "Main_port_name" <> 'JURONG ISLAND'
    ORDER BY
    distance_in_kilometers
    LIMIT 5;
    """

    query2 = """
    SELECT
    "Wpi_country_code" AS country,
    COUNT(*) AS port_count
    FROM
    wpi_data_tbl
    WHERE
    "Load_offload_wharves" = 'Y'
    GROUP BY
    "Wpi_country_code"
    ORDER BY
    port_count DESC
    LIMIT 1;
    """

    query3 = """
    SELECT
    "Wpi_country_code" AS country,
    "Main_port_name" AS port_name,
    "Latitude_degrees" AS port_latitude,
    "Longitude_degrees" AS port_longitude

    FROM
    wpi_data_tbl
    WHERE
    "Supplies_provisions" = 'Y' AND
    "Supplies_water" = 'Y' AND
    "Supplies_fuel_oil" = 'Y' AND
    "Supplies_diesel_oil" = 'Y'
    ORDER BY
    (haversine(CAST("Latitude_degrees" AS float),
    CAST("Longitude_degrees" AS float),
    CAST(1.0 AS float),
    CAST(1.0 AS float)))
    LIMIT 1;
    """

    # Execute the queries
    cur = conn.cursor()
    cur.execute(create_function_query)
    cur.execute(query1)
    results1 = cur.fetchall()
    cur.execute(query2)
    results2 = cur.fetchall()
    cur.execute(query3)
    results3 = cur.fetchall()

    # Print the results
    for row in results1:
        print(row)

    for row in results2:
        print(row)

    for row in results3:
        print(row)

    # Close the connection
    conn.close()
