# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:24:01 2021

@author: 91799
"""
def div(a,b):
    print(a/b)
    
    
def smart_div(func):
    
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div = smart_div(div)


div(2,4)



def inc(x):
    return x+1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc,3))


def print_msg(message):
    greeting="hello"
    def printer():
        print(greeting, message)
    return printer
func = print_msg("python is awesome")
func()


def printer():
    print("Hello Worl!")
def display_func(func):
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("finished execution")
    return inner

dec_fun = display_func(printer)
dec_fun()



