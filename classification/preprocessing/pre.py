import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer




class Preprocess:
    def __init__(self,dataFrame):
        self.data = dataFrame
    def preprocess(self):
        self.imputer  = Imputer()
    @property
    def pdf(self):
        return self.data
        






# loading the data
data = pd.read_csv("Data.csv")
pre = Preprocess(data)
print(pre.pdf)
