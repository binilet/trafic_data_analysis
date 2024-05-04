from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG('data_test_pipeline',start_date=datetime(2024,5,1),schedule_interval=None) as dag:
    run_custom_dbt_tests = BashOperator(
        task_id='run_custom_dbt_tests',
        bash_command='dbt test --profiles-dir /app/dbt/ --project-dir /app/dbt/',
    )

    run_custom_dbt_tests
