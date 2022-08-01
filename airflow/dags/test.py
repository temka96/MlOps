from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'depends_on_past': False,}

with DAG(
    'test_dag',
    default_args=default_args,
    schedule_interval='@once',
    catchup=False
) as dag:

    t1 = BashOperator(
        task_id='echo_hi', 
        bash_command='echo "Hello"',
    )
   
    t2 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t3 = BashOperator(
        task_id='ls',
        bash_command='ls -la',
    )

    t4 = BashOperator(
        task_id='pwd',
        bash_command='pwd',
    )

    t1 >> t2
    t1 >> t3
    t3 >> t4
    t2 >> t4

