import requests
import psycopg2
from datetime import datetime
from psycopg2 import sql

def extract_data():
    response = requests.get('https://randomuser.me/api/?results=100')
    data = response.json()
    return data['results']

def transform_data(data):
    transformed_data = []
    for record in data:
        dob = datetime.strptime(record['dob']['date'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d')
        transformed_record = (
            record['name']['first'],
            record['name']['last'],
            record['gender'],
            record['email'],
            dob,
            record['location']['country'],
            record['location']['street']['name'],
            record['location']['city'],
            record['location']['state'],
            record['location']['postcode'],
            record['phone'],
            record['cell']
        )
        transformed_data.append(transformed_record)
    return transformed_data

def load_data(data):
    conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            gender VARCHAR(10),
            email VARCHAR(100),
            dob DATE,
            country VARCHAR(50),
            street VARCHAR(100),
            city VARCHAR(50),
            state VARCHAR(50),
            postcode VARCHAR(20),
            phone VARCHAR(20),
            cell VARCHAR(20)
        )
    """)
    insert = sql.SQL('INSERT INTO users VALUES {}').format(
        sql.SQL(',').join(map(sql.Literal, data))
    )
    cur.execute(insert)
    conn.commit()
    cur.close()
    conn.close()

def etl():
    data = extract_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)

etl()


from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 1),
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'user_etl', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag)

t2 = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    provide_context=True,
    dag=dag)

t3 = PythonOperator(
    task_id='load',
    python_callable=load_data,
    provide_context=True,
    dag=dag)

t1 >> t2 >> t3
