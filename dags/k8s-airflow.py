from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "hello_world",
    default_args=default_args,
    description="A simple DAG to print Hello, World!",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:
    t1 = BashOperator(
        task_id="print_hello_world",
        bash_command='echo "Hello, World!"',
    )

