# Datapipeline with 
# 
# 
import io
import os
import requests
import subprocess
import pandas as pd
from datetime import datetime
from prefect import flow, task
from hydra import compose, initialize
from sklearn.model_selection import train_test_split


@task
def directory_mapping():
    """
    Move to specific folder from the root since current kind of monorepo for everything
    run on the root.
    TODO: Test - may require config checking for both git and dvc in the beginning 
    """
    print("Current working directory:", os.getcwd())
    try:
        os.chdir("pipe/pipeline_dev/DataPipeline")
    except Exception as e:
        print("Unable to change directory, error -", e)
    print("Working dir changed to -", os.getcwd())


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
    """
    Code to store the data into directories.
    Generate train, test, valid datasets and store it in respective folders
    Add files to DVC
    Committing changes with git.
    Note
    ---
    All operation with the dvc and git are done with subprocess.
    A separate file tag.md created and initiated with V0.1 in the DVC directory, manually
    tag.md currently only update the last part [need to change.]
    TODO : control all the configuration with hydra. test_size, folders, versioning files.
    """
    print("working directory:", os.getcwd())
    print("Input data shape:", data.shape)
    features = data.iloc[:,:-1]
    labels = data.iloc[:,-1]
    # splits does not contains random state since we need different data at 
    # each run for testing with DVC.
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
    x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.1)

    # TODO move to hydra
    train_path = "data/train"
    test_path = "data/test"
    valid_path = "data/valid"
    paths = [train_path, test_path, valid_path]
    # saving the data into corresponding paths. generating the folder structure if not exists as well.
    for path in paths:
        full_path = os.path.join(os.getcwd(), os.path.normpath(path))
        print(full_path)
        if not os.path.exists(full_path):
            print('path not exists, creating')
            os.makedirs(full_path)
        if "train" in path:
            x_train.to_csv(os.path.join(full_path, "x_train.csv"),index=False)
            y_train.to_csv(os.path.join(full_path, "y_train.csv"),index=False)
        elif "test" in path:
            x_test.to_csv(os.path.join(full_path, "x_test.csv"),index=False)
            y_test.to_csv(os.path.join(full_path, "y_test.csv"),index=False)
        elif "valid" in path:
            x_valid.to_csv(os.path.join(full_path, "x_valid.csv"),index=False)
            y_valid.to_csv(os.path.join(full_path, "y_valid.csv"),index=False)
    
    # moving to data folder for executing dvc.
    os.chdir("data/") # current one is DVC_lr and dvc init in DVC_lr/data
    items = [
        'train/x_train.csv',
        'train/y_train.csv',
        'test/x_test.csv',
        'test/y_test.csv',
        'valid/x_valid.csv',
        'valid/y_valid.csv'
    ]
    # adding the data to dvc
    for item in items:
        cmd = f"dvc add {item}"
        try:
            result = subprocess.run(cmd, shell=True, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            if result.returncode == 0:
                print(f"Data versioned for item {item}")
            else:
                print(f"Error in adding to DVC : {result.stderr}")
        except subprocess.CalledProcessError as e:
            print(f"Error {e.returncode}\n {e.stderr}")
        except Exception as e:
            print(f"Error in processing {str(e)}")
    
    items = [
    'train/x_train.csv.dvc',
    'train/y_train.csv.dvc',
    'test/x_test.csv.dvc',
    'test/y_test.csv.dvc',
    'valid/x_valid.csv.dvc',
    'valid/y_valid.csv.dvc'
    ]   
    # time component for commit message.
    time_component = datetime.today().__str__().split()[0]
    with open("tag.md") as fp:
        tag_data = fp.read()
    td = tag_data[1:].split(".")
    td[1] = int(td[1]) + 1 # for simplicity only updating the 
    td = f"V{'.'.join([str(i) for i in td])}"

    commit_msg = f"{td}-{time_component}"
    # adding and commit the files.
    try:
        result = subprocess.run(["git", "add", *items], shell=True, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        if result.returncode == 0:
            result = subprocess.run(["git", "commit", "-m", commit_msg], shell=True, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            print("data versioned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error {e.returncode}\n {e.stderr}")
    except Exception as e:
        print(f"Error in processing {str(e)}")
    
    # update version tagging file
    with open("tag.md","w") as fp:
        fp.write(td)


@flow(name="Data Pipeline", log_prints=True)
def data_loading(cfg_datapipe={}):
    """
    load the preprocessed data into the directory.
    """
    if not cfg_datapipe:
        initialize(config_path="conf", version_base=None)
        cfg = compose(config_name="staging")
        cfg_datapipe = cfg.datapipe
    directory_mapping()
    raw_data = gather_data(url=cfg_datapipe.get('url'))
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)

if __name__ == "__main__":
    data_loading()
