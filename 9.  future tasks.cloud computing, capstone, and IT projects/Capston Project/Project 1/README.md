## Covid-19 Data Analysis

This project is a Python script that creates a PostgreSQL database, imports a CSV file containing Covid-19 data into the database, and then performs various SQL queries to analyze the data.
## Requirements
    Python 3.6+
    PostgreSQL
    pandas
    sqlalchemy
    psycopg2
    Installation

## Clone the repository:

    git clone https://github.com/EbejaleKasimir/covid-19-data-analysis.git

## Install the required Python packages:

    pip install pandas sqlalchemy psycopg2-binary

## Usage

    Make sure PostgreSQL is running on your machine.
    Update the PostgreSQL connection parameters in the script if necessary. The default parameters are:
    user: "postgres"
    password: "demopass"
    host: "localhost"
    port: "5432"
    database: "postgres"
## Run the script:

    python covid_19_data_analysis.py

## How it Works
## The script performs the following steps:
1.  Creates a new PostgreSQL database named "covid_19_data".
2.  Reads a CSV file named "Covid_19_data.csv" into a pandas DataFrame.
3.  Converts the 'ObservationDate' column to datetime format.
4.  Writes the DataFrame to the new database, replacing any existing table with the same name.
5.  Connects to the new database and creates a cursor object.
6.  Executes a list of SQL queries to analyze the Covid-19 data. The queries calculate the total number of confirmed    cases, deaths, and recoveries; the total number of each by year and country; the percentage increase in deaths from 2019 to 2020; the five countries with the most confirmed cases; and the net change in confirmed cases by year and month.
7.  Prints the results of each query.

## Troubleshooting

If you encounter an error while creating the database, make sure PostgreSQL is running and the connection parameters are correct. If the error persists, check the PostgreSQL documentation and the psycopg2 documentation for possible solutions.

If you encounter an error while reading the CSV file or writing to the database, make sure the file is in the correct format and the 'ObservationDate' column can be converted to datetime format. If the error persists, check the pandas documentation and the sqlalchemy documentation for possible solutions.

If you encounter an error while executing the SQL queries, make sure the queries are correctly formatted and the table and column names match those in the database. If the error persists, check the PostgreSQL documentation for possible solutions.
