import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
# import the module spliting the dataset
from sklearn.model_selection import train_test_split


data = pd.read_csv("Social_Network_Ads.csv")
# print(data)
'''
the dataset contains the data collected of people who can buy a suv
the prediction has take place by using two independent properties which is age and
salary 
finding out the correlation between the age and salary and corresponding output



'''

# setting up the the feature as well as the class matrices
x = data.iloc[:,[2,3]].values
y = data.iloc[:,4].values

#Spliting the dataset for testing and training . 100 elements for testing 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .25,random_state=0)

# scaling the feature matrix 
from sklearn.preprocessing import StandardScaler

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

# fitting the model with the sklearn.linearmodel.LogisticRegression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train,y_train)
y_predicet = classifier.predict(x_test)


# creating the confussion_matric for evaluating the prediction
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_predicet)



