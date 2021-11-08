# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:01:41 2021

@author: 91799
"""
import numpy as np
import pandas as pd

data = np.array([['col0', 'col1', 'col2'],['row1', 1,2],['row2', 5, 7]])
print(data)

print(pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:]))

my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(my_2darray)
# Take a dictionary as input to your DataFrame 
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
print(my_dict)
# Take a DataFrame as input to your DataFrame 
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print(my_df)
# Take a Series as input to your DataFrame
my_series = pd.Series({"Belgium":"Brussels", "India":"New Delhi", "United Kingdom":"London", "United States":"Washington"})
print(my_series)


df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), index= [2, 'A', 4],
                  columns=['s', 'k', 'b'])

print(df)
# Pass `2` to `loc`
print(df.loc[2])

# Pass `2` to `iloc`
print(df.iloc[2])

#deleting index from df

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]), 
                  index= [2.5, 12.6, 4.8, 4.8, 2.5], 
                  columns=[48, 49, 50])
                  
print(df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index'))
