import pandas as pd
import matplotlib.pyplot as plt
import numpy as nm
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# reading data
df = pd.read_csv('eurovision.csv')
print(df.head(3))
