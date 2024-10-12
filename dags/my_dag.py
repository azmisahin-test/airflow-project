from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def my_task():
    print("Task executed!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
}

with DAG('my_first_dag', default_args=default_args, schedule_interval='@daily') as dag:
    start = DummyOperator(task_id='start')
    task = PythonOperator(task_id='my_task', python_callable=my_task)
    end = DummyOperator(task_id='end')

    start >> task >> end
