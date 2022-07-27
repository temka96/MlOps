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
    t1 >> t2