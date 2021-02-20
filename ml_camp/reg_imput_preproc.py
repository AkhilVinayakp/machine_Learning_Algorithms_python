'''
Regression model  with preprocessing (Imputer) pipeline
'''
from math import pi
from os import pipe
from pandas.io.parquet import FastParquetImpl
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
# loading the model
from sklearn.linear_model import LogisticRegression
import pandas as pd
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# loading data
df = pd.read_csv('diabetes.csv')
y = df['Outcome'].values
X = df.iloc[:,:-1].values
print(df.shape,X.shape)
logging.debug(f"{df.columns}")
logging.debug(f"{df.isnull().values.any()}")
# initializing the imp
imp = SimpleImputer(missing_values='NaN',strategy='mean', copy=False)
# creating the model
logreg = LogisticRegression()
steps = [('imputation',imp),('Log_reg',logreg)]
pipe = Pipeline(steps=steps)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.4, random_state = 42)

pipe.fit(X_train,y_train)
y_pred = pipe.predict(X_test)
print(pipe.score(X_test,y_test))

