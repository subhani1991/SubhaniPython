# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:46:39 2021

@author: 91799
"""
def add(x,y):
    print("print the adding of two elements:")
    
    return x+y
#print(add(5,10))

def sub(a,b):
    print("subtraction:---")
    return a-b
#print(sub(30,20))

def mul(c,d):
    return c*d
#print(mul(10,20))

def div(a,b):
    if b==0:
        raise ValueError("can not be divided by zero")
    return a/b
#print(div(8,2))