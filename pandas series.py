# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:43:07 2021

@author: 91799
"""
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)

#import the pandas library and aliasing as pd

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print (s)

s = pd.Series(5, index=[0, 1, 2, 3])
print (s)

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print(s[0])
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first three element
print(s[:3])
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the last three element
print (s[-3:])

s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve a single element
print (s['a'])
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve multiple elements
print (s[['a','c','d']])
