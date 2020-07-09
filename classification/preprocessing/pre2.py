#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:03:48 2020
preprocessing Template with sklearn

@author: po
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.compose import ColumnTransformer


class Preprocess:
    def __init__(self,data):
        self.data = pd.read_csv(data)
    @property
    def frm(self):
        return self.data
    @property   
    def check_nan(self, pri_data=False):
        self.nan_col=[]
        for i in self.data.columns:
            l = list(self.data[i].isnull())
            if any(l):
                self.nan_col.append(i)
        return self.nan_col
    def clean_nan(self):
        imputer = SimpleImputer()# leaving with default
        if len(self.nan_col) == 0:
            return 0
        self.data[self.nan_col] = imputer.fit_transform(self.data[self.nan_col])
    
    def enc_cat_data(self,index = 0):
        label = LabelEncoder()
        self.data.iloc[:,index] = label.fit_transform(self.data.iloc[:,index])
    def enc_cat_hot(self,index=0):
        onehot = OneHotEncoder(categorical_features=[0])
        self.data = onehot.fit_transform(self.data)
    def cl_transform(self,li):
        transformer =  ColumnTransformer(transformers=li, remainder="passthrough")
        self.data = pd.DataFrame(transformer.fit_transform(self.data))
        #print(transformer.get_params())
        
    

data = Preprocess("Data.csv")
print(data.frm)
print(data.check_nan)
data.clean_nan()
print(data.frm)
#data.enc_cat_data()
#data.enc_cat_hot()

# defining the list of transforms 
t = [('one',OneHotEncoder(),[0])]
data.cl_transform(t)

print(data.frm)

