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

# %%
