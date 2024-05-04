from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, text
import os

def init_pipeline():
    print('initalization of pipeline ...')
    print(f"Current working directory: {os.getcwd()}")

def create_staging_table():
    engine = create_engine('postgresql://postgres:123@postgres/traffic_data_db')
    create_table_query = """
    CREATE TABLE IF NOT EXISTS staging_traffic_data (
        data TEXT
    );
    """
    with engine.begin() as connection:
        connection.execute(text(create_table_query))

def load_csv_to_staging():
    print('loading csv skipped for now; since it is already loaded')
    # df = pd.read_csv('/data/20181024_d1_0830_0900.csv',header=None,names=['data'])
    # engine = create_engine('postgresql://postgres:123@postgres/traffic_data_db')
    # #load the dataframe into the staging table
    # df.to_sql('staging_traffic_data',engine,if_exists='replace',index=False,chunksize=1000)

with DAG('traffic_data_pipeline',start_date=datetime(2024,5,1),schedule_interval=None) as dag:
    init_pipeline = PythonOperator(
        task_id='init_pipeline',
        python_callable=init_pipeline
    )

    # create_database = PythonOperator(
    #     task_id='create_database',
    #     python_callable=create_database
    # )

    # update_dbt_config = PythonOperator(
    #     task_id='update_dbt_config',
    #     python_callable=update_dbt_config
    # )

    create_staging_table = PythonOperator(
        task_id='create_staging_table',
        python_callable=create_staging_table
    )

    load_csv = PythonOperator(
        task_id='load_csv_to_staging',
        python_callable=load_csv_to_staging
    )

    run_dbt_transformation = BashOperator(
        task_id='run_dbt_transformations',
        bash_command='dbt run --profiles-dir /app/dbt/ --project-dir /app/dbt/',
        
    )

    init_pipeline >> create_staging_table >> load_csv >> run_dbt_transformation