# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 14:07:09 2021

@author: 91799
"""
def fibonacci(n, value_dict):
    # the first two values of fibonacci is always 0,1
    if n == 0 or n == 1:
        return n
    # if fibonacci(n) is already calculated then return it from dict 
    if value_dict.get(n):
        return value_dict[n]
    #else store it in dict and return next time it is called for.
    else:
        value_dict[n] = fibonacci(n-2,value_dict) + fibonacci(n- 
        1,value_dict)
        return value_dict[n]

print(fibonacci(100, {}))