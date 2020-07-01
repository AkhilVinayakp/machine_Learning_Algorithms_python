import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer




class Preprocess:
    def __init__(self,dataFrame):
        self.data = dataFrame
        # setting up the independ values into features
    @property
    def features(self):
        return self.x
    @features.setter
    def features(self,x):
        self.x = x
    @property
    def labels(self):
        return self.y
    @labels.setter
    def labels(self,y):
        self.y = y
    # preprocess the data
    def preprocess(self):
        self.imputer  = SimpleImputer()
        
    @property
    def pdf(self):
        return self.data
        






# loading the data
data = pd.read_csv("Data.csv")
pre = Preprocess(data)

print(pre.pdf)

pre.features = data.iloc[:,:-1].values
pre.labels = data.iloc[:,3].values
print(pre.features, pre.labels)



