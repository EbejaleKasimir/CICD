
# PostgreSQL Database Creation and Operation

This Python script is designed to create a PostgreSQL database, load data from an Access database into it, and execute SQL queries from a file.

## Prerequisites

- Python 3.6 or higher
- PostgreSQL server
- Python packages: os, pandas, sqlalchemy, psycopg2, pyodbc

## Installation

1. Clone the repository to your local machine.
2. Install the required Python packages using pip:

bash
pip install pandas sqlalchemy psycopg2-binary pyodbc


## Usage

1. Update the PostgreSQL server connection details in the script (user, password, host, port, database).
2. Update the Access database file path in the script.
3. Update the SQL file path in the script.
4. Run the script:

bash
python Geo_sql_embed.py


## Functions

- `create_database(database_name)`: Creates a new PostgreSQL database.
- `split_sql_file(filename)`: Splits a SQL file into separate commands.
- `is_inside_string(stmt)`: Checks if a statement is inside a string.
- `execute_sql_file(filename)`: Executes a SQL file.

## Workflow

1. The script first creates a new PostgreSQL database using the `create_database` function.
2. It then creates a SQLAlchemy engine to interact with the newly created database.
3. The script reads data from an Access database file into a pandas DataFrame.
4. The data is then loaded into the PostgreSQL database.
5. Finally, the script executes SQL commands from a file using the `execute_sql_file` function for the Geo.py or within the Geo_sql_embed.py file.  

## Notes

- The script assumes that the PostgreSQL server is running on localhost at port 5432.
- The script uses the psycopg2 package for PostgreSQL operations and pyodbc for Access database operations.
- The script uses pandas for data manipulation and SQLAlchemy for database operations.
- The script assumes that the Access database file and the SQL file are in the same directory as the script.
- The script prints the output of the SQL commands to the console.
