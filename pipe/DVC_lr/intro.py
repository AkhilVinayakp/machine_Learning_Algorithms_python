#%%
import pandas as pd
import os
# %%
print("cwd :", os.getcwd())
# %%
data = pd.read_csv("../pipeline_dev/DataPipeline/data/wine.csv")
# %%
data.shape
# %%
# splitting the data into train, test, validation
from sklearn.model_selection import train_test_split

features = data.iloc[:,:-1]
labels = data.iloc[:,-1]
# %%
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
# %%
x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.1)
# %%
train_path = "data/train"
test_path = "data/test"
valid_path = "data/valid"
paths = [train_path, test_path, valid_path]

# %%
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

# %%
# adding everything to dvc as well
import subprocess

# going to the directory where dvc is initialized
os.chdir("data/") # current one is DVC_lr and dvc init in DVC_lr/data
items = [
    'train/x_train.csv',
    'train/y_train.csv',
    'test/x_test.csv',
    'test/y_test.csv',
    'valid/x_valid.csv',
    'valid/y_valid.csv'
]
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



# %%
