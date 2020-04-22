#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:55:35 2020

@author: po
"""
import pandas as pd
import numpy as np
#from math import sqrt do not use math.sqrt cause error  can not convert the series to class float


# creating Ml classf
class Ml:
    def __init__(self):
        pass
    def add_data(self):
        try:
            self.name = input('Enter the name :::')
            self.height = int(input('enter the height :::'))
            self.weight = int(input('enter the weight :::'))
        except (IOError, TypeError, KeyboardInterrupt) as e:
            print(e)
        except Exception as e:
            print(e)
    def __eucli(self):#return the euclidien distance of each elements from the given as a dataframe
        #self.data['eucli']=self.data['eucli'].astype(float)
        #print(self.data)
        self.data['eucli'] = np.sqrt((self.height-self.data['height'])**2+(self.weight-self.data['weight'])**2).astype(float)
        #print(self.data)
    
    def __select_k(self):# return the k neighbour
        pass
    #fn that calculate the class of given data
    def __ret_class(self):
        pass
    #fn run will bw called from outside
    def run(self,k):
        self.k = k # amount of neightbour selection
        self.data = pd.DataFrame(pd.read_csv("data.csv"))
       # print(self.data)
        self.__eucli()
        print(self.data)
        
        
    

def initial():
    try:
        ml = Ml()
        ml.add_data()
        ml.run(3)
    except Exception as e:
        print(e)

initial()
        


'''
data = pd.read_csv("data.csv")
print(data)
'''