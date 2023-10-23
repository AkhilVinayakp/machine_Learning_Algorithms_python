# Datapipeline with 
# 
# 
import requests
import io
import os
import pandas as pd
from prefect import flow, task

@task(retries=3, retry_delay_seconds=5)
def gather_data(url:str)->pd.DataFrame:
    """
    Get data from the given url
    """
    print("Loading data from external source")
    try:
        response = requests.get(url=url)
        print("Response: ", response.status_code)
        response.raise_for_status()
        data = pd.read_csv(io.StringIO(response.text))
        return data
    except Exception as e:
        print("Error in loading the data: ", e)
        raise Exception("Data loading Issue terminating.")


@task
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

@task
def load_data(data:pd.DataFrame):
    # Add code to load the transformed data to the destination
    print("data loaded to destination")
    print("working dir :", os.getcwd())
    print("data available:", data.shape)
    print(data.to_csv("wine.csv", index=False))
    return

@flow(name="Data Pipeline", log_prints=True)
def data_loading(input_url:str):
    """
    load the preprocessed data into the directory.
    """
    raw_data = gather_data(url=input_url)
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)


if __name__ == "__main__":
    url = "https://gist.githubusercontent.com/tijptjik/9408623/raw/b237fa5848349a14a14e5d4107dc7897c21951f5/wine.csv"
    # my_flow = data_loading(input_url=url)
    # print(my_flow)
    
