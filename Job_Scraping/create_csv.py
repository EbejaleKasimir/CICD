import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:P%4055w076@localhost/cohort_4_')

# Execute SQL query and load the result into a pandas DataFrame
df = pd.read_sql_query('SELECT * FROM data_engineering_jobs', con=engine)

# Write DataFrame to CSV file
df.to_csv('data_engineering_jobs.csv', index=False)
