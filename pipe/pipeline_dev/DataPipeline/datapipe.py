from airflow import DAG
# from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import io
import pandas as pd
import os

# Define default_args for the DAG
default_args = {
    'owner': 'AK',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create a DAG instance
dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='Data Pipeline Orchestration',
    schedule_interval=timedelta(days=1),  # Set the schedule interval (daily in this case)
    catchup=False,  # Prevent backfilling for this example
)

# Define Python functions for tasks
def extract_data():
    # Add code to extract data from source
    print("Loading data from external source")
    try:
        response = requests.get("https://gist.githubusercontent.com/tijptjik/9408623/raw/b237fa5848349a14a14e5d4107dc7897c21951f5/wine.csv")
        print("Respone: ", response.status_code)
        response.raise_for_status()
        data = pd.read_csv(io.StringIO(response.text))
        return data
    except Exception as e:
        print("Error in loading the data: ", e)
        raise Exception("Data loading Issue terminating.")

def transform_data(data:pd.DataFrame):
    # Add code to transform the extracted data
    print("Applying data transformation")
    label_mapping = {
    1: 'class_1',
    2: 'class_2',
    3: 'class_3'
    }
    column_names = {"Malic.acid":"Malic_acid", "Nonflavanoid.phenols": "NF_phenols", "Color.int": "Color_int"}
    data['wine_class'] = data['Wine'].replace(label_mapping)
    data.drop('Wine', inplace=True, axis=1)
    data = data.rename(columns=column_names)
    return data

def load_data(data:pd.DataFrame):
    # Add code to load the transformed data to the destination
    print("data loaded to destination")
    print("working dir :", os.getcwd())
    print("data available:", data.shape)

# Define task instances
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    op_args=[extract_data.output],
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    op_args = [transform_task.output],
    dag=dag,
)

# Set task dependencies
extract_task >> transform_task >> load_task
