# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:36:11 2021

@author: 91799
"""


#global keywords

c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)