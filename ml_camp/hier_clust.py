"""
Hierarchical clustering 
with alggomerative method
visualizing the dentogram
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as nm
import logging
from pandas.io.parsers import read_csv
import scipy
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

class Hier:
    def __init__(self) -> None:
        self.data = pd.read_csv('eurovision.csv')
    def __str__(self):
        return str(self.data.info())
    def explore(self):
        print(self.data.head(3))
        print("Tail of data")
        print(self.data.tail(3))
    def pre(self):
        # checking for clumns contains any NaN
        if any(self.data.isnull()):
            self.data.dropna()
            print('Droped')


    # def create_d(self):

    