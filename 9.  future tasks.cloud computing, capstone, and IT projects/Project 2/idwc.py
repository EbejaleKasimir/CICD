import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker 
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

from sqlalchemy import text

def split_sql_file(filename):
    data = open(filename, 'r').read()
    stmts = data.split(';')
    chunks = []
    chunk = ''
    for stmt in stmts:
        if stmt.strip().endswith('$$ LANGUAGE plpgsql'):
            chunk += stmt + ';'
            chunks.append(chunk)
            chunk = ''
        elif chunk or is_inside_string(stmt):
            chunk += stmt + ';'
        else:
            chunks.append(stmt + ';')
    return chunks

def is_inside_string(stmt):
    count_single_quote = stmt.count("'")
    count_double_quote = stmt.count('"')
    return count_single_quote % 2 != 0 or count_double_quote % 2 != 0

def execute_sql_file(filename):
    # Connect to your postgres DB
    conn = psycopg2.connect(user="postgres", password="demopass", host="localhost", port="5432", database="wpi_data")
    
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sql_file = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sql_commands = sql_file.split(';')

    # Execute every command from the input file
    cur = conn.cursor()
    for command in sql_commands:
        # This will skip and report errors (you can change the code to stop at errors if you want)
        try:
            cur.execute(command)
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: ", error)
        
        # Commit changes
        conn.commit()

    cur.close()
    conn.close()


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


# # Execute SQL file
# execute_sql_file(current_dir + '/project_2_query.sql')

import psycopg2

# Connect to the database
conn = psycopg2.connect(database="wpi_data", user="postgres", password="demopass")

# Open the SQL file
with open("project_2_query.sql") as sql_file:
    sql_query = sql_file.read().split(";")

# Execute the SQL commands one by one
for command in sql_query:
    cur = conn.cursor()
    cur.execute(command)

# Print the output
results = cur.fetchall()
for row in results:
    print(row)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

