#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:55:35 2020

@author: po
"""
import pandas as pd
from math import sqrt


# creating Ml class
class Ml:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    def __eucli(self):#return the euclidien distance of each elements from the given as a dataframe
        self.data['eucli'] =(sqrt((self.height-self.data['height'])**2+(self.weight-self.data['weight'])**2)).astype(float)
        print(self.data)
    
    def __select_k(self):# return the k neighbour
        pass
    #fn that calculate the class of given data
    def __ret_class(self):
        pass
    #fn run will bw called from outside
    def run(self,k):
        self.k = k # amount of neightbour selection
        self.data = pd.DataFrame(pd.read_csv("data.csv"))
        print(self.data)
        self.__eucli()
        print(self.data)
        
        
    

def initial():
    name = input('Enter the name')
    height = int(input('enter the height'))
    weight = int(input('enter the weight'))
    try:
        ml = Ml(name,height,weight)
        ml.run(3)
    except Exception as e:
        print(e)


initial()
        


'''
data = pd.read_csv("data.csv")
print(data)
'''