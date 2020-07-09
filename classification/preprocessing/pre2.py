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
        



data = Preprocess("Data.csv")
print(data.frm)
print(data.check_nan)
