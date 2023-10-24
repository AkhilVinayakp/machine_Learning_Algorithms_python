# Datapipeline with 
# 
# 
import requests
import io
import os
from hydra import compose, initialize
import pandas as pd
from prefect import flow, task
from sklearn.model_selection import train_test_split


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
    features = data.iloc[:,:-1]
    labels = data.iloc[:,-1]
    # splitting the data
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
    # random state avoided for the purpose to get different dataset.
    # for testing with dvc
    x_train, x_test, val_train, val_test = train_test_split(x_train, y_train, test_size=0.1)
    # random state not considers for dvc testing.
    # test : 20% train:70% validation:10%
    
    # TODO
    # * add following to config
    train_path = "data/train"
    test_path = "data/test"
    val_path = "data/val"
    # generating those paths and files
    rpaths=[train_path, test_path, val_path]
    try:
        for rpath in rpaths:
            full_path = os.path.join(os.getcwd(), rpath)
            if not os.path.exists(full_path):
                # creating:
                os.makedirs(full_path)
                print("created path ", full_path)
    except Exception:
        print("path can not be created/accessible.")
        raise Exception("end point path creation failed")
    # writing the files to the path
    # TODO
    



    print(data.to_csv("wine.csv", index=False))
    return

@flow(name="Data Pipeline", log_prints=True)
def data_loading(cfg_datapipe={}):
    """
    load the preprocessed data into the directory.
    """
    if not cfg_datapipe:
        initialize(config_path="conf", version_base=None)
        cfg = compose(config_name="staging")
        cfg_datapipe = cfg.datapipe
    raw_data = gather_data(url=cfg_datapipe.get('url'))
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)

if __name__ == "__main__":
    data_loading()
