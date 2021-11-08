# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:16:42 2021

@author: 91799
"""
# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

#pass statement
number = 0

for number in range(10):
    if number == 5:
        pass    # pass here

    print('Number is ' + str(number))

print('Out of loop')