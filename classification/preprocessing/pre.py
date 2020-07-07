import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.preprocessing import Imputer  >>>deprecation 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder






# loading the data
data = pd.read_csv("Data.csv")
pre = Preprocess(data)

#print(pre.pdf)

pre.features = data.iloc[:,:-1]
pre.labels = data.iloc[:,3]
pre.check_nan()
pre.preprocess()
pre.enc_cat_lab(0)
pre.enc_cat_mr(0)
#print(pre.features, pre.labels)
print(pre.check_nan())




