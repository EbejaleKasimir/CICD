import requests
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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

        # Execute the CREATE DATABASE statement
        cur.execute(f"CREATE DATABASE {database_name};")

        # Close the cursor and the connection
        cur.close()
        conn.close()

        print(f"Database {database_name} created successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error occurred while creating database {database_name}. Error message: {error}")

if __name__ == "__main__":
    database_name = "covid_19_data"
    create_database(database_name)

# Define the connection string
database_url = "postgresql://postgres:demopass@localhost:5432/covid_19_data"

# Create the SQLAlchemy engine
engine = create_engine(database_url)

# Read the CSV file
data = pd.read_csv("Covid_19_data.csv")

# Convert 'ObservationDate' to datetime
data["ObservationDate"] = pd.to_datetime(data["ObservationDate"])

# Write the data to the database
data.to_sql("covid_19_data", engine, if_exists='replace', index=False)

# Connect to the database
conn = psycopg2.connect(
    user="postgres",
    password="demopass",
    host="localhost",
    port="5432",
    database=database_name
)

# Create a cursor object
cur = conn.cursor()

# List of SQL queries


queries = [
    """
    SELECT SUM("Confirmed"), SUM("Deaths"), SUM("Recovered")
    FROM covid_19_data;
    """,
    """
    SELECT EXTRACT(YEAR FROM "ObservationDate") AS Year, 
           SUM("Confirmed"), SUM("Deaths"), SUM("Recovered")
    FROM covid_19_data
    WHERE EXTRACT(MONTH FROM "ObservationDate") BETWEEN 1 AND 3
    GROUP BY Year;
    """,
    """
    SELECT "Country", 
           SUM("Confirmed") AS Total_Confirmed, 
           SUM("Deaths") AS Total_Deaths, 
           SUM("Recovered") AS Total_Recoveries
    FROM covid_19_data
    GROUP BY "Country";
    """,
    """

    WITH "Deaths" AS (
      SELECT EXTRACT(YEAR FROM "ObservationDate") AS Year, 
             SUM("Deaths") AS Total_Deaths
      FROM covid_19_data
      GROUP BY Year
    )

    SELECT (d2.Total_Deaths - d1.Total_Deaths) / d1.Total_Deaths * 100 AS Percentage_Increase
    FROM "Deaths" d1, "Deaths" d2
    WHERE d1.Year = 2019 AND d2.Year = 2020;
    """,

    """
    SELECT "Country", SUM("Confirmed") AS Total_Confirmed
    FROM covid_19_data
    GROUP BY "Country"
    ORDER BY Total_Confirmed DESC
    LIMIT 5;
    """,

    """
    SELECT EXTRACT(YEAR FROM "ObservationDate") AS Year, 
           EXTRACT(MONTH FROM "ObservationDate") AS Month, 
           SUM("Confirmed") - LAG(SUM("Confirmed")) OVER (ORDER BY EXTRACT(YEAR FROM "ObservationDate"), EXTRACT(MONTH FROM "ObservationDate")) AS Net_Change
    FROM covid_19_data
    GROUP BY Year, Month;
    """
]

# Execute each query and print the results
for query in queries:
    cur.execute(query)
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
    print(df)
