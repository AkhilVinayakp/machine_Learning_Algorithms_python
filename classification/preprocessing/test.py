#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 12:40:01 2020

@author: po
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,LabelEncoder

data = pd.read_csv("Data.csv")

labenc = LabelEncoder()
data.iloc[:,0] = labenc.fit_transform(data.iloc[:,0])

print(data)
'''
onehotencoder = OneHotEncoder(categorical_features=0)
data = onehotencoder.fit_transform(data)
print(data)
'''