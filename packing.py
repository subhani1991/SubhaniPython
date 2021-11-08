# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:30:56 2020

@author: 91799
"""


#packing
def my_fun(a,b):
    result=a+b
    print(result)
my_fun(10,20)
print(my_fun)


def add_num(*args):
    print(sum(args))
add_num(1,2,3,10,20)
print(add_num)


#unpacking

def my_fun(*var):
    print(var)
    print(sum(var))
my_list=[10,20,30,40]
my_fun(*my_list)
print(my_fun)


#packing and unpacking with dict objects

def contact_info(*args):
    print(args)
    #print(sum(args))
contact_list=('jan', 'shaik', 'subhani')
contact_list_1=(10,20,30,40)
contact_info(*contact_list)
print(contact_info(contact_list_1))


def my_dict(**vars):
    print(vars)
my_dict(shaik=28, mabbu=26, hannu=8)
print(my_dict)


#iterators
a=[4,0,10,5]
for i in (a):
    print(i)
    
    
