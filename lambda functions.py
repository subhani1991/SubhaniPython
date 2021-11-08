# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:30:19 2021

@author: 91799
"""
# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)


# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)