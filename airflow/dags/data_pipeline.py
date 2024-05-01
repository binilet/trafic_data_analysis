from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

def load_csv_to_staging():
    df = pd.read_csv('../data/20181024_d1_0830_0900.csv',header=None,names=['data'])
    engine = create_engine('postgresql://postgres:123@postgres/postgres')
    #load the dataframe into the staging table
    df.to_sql('staging.traffic_data',engine,if_exists='replace',index=False,chunksize=1000)

with DAG('traffic_data_pipeline',start_date=datetime(2024,5,1),schedule_interval=None) as dag:
    load_csv = PythonOperator(
        task_id='load_csv_to_staging',
        python_callable=load_csv_to_staging
    )

    run_dbt_transformation = BashOperator(
        task_id='run_dbt_transformations',
        bash_command='dbt run --models +traffic_data_general +traffic_data_locations'
    )

    load_csv >> run_dbt_transformation