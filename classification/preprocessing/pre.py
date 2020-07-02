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
    # check for nan data column in dataframe
    def check_nan(self, pri_data=False):
        self.nan_col=[]
        for i in self.x.columns:
            l = list(self.x[i].isnull().values)
            if any(l):
                self.nan_col.append(i)
        return self.nan_col
    
    # preprocess the data
    def preprocess(self):
        self.imputer  = SimpleImputer()
        
        
        
        
    @property
    def pdf(self):
        return self.data
        






# loading the data
data = pd.read_csv("Data.csv")
pre = Preprocess(data)

#print(pre.pdf)

pre.features = data.iloc[:,:-1]
pre.labels = data.iloc[:,3]
#print(pre.features, pre.labels)

print(pre.check_nan())



