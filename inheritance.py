# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:32:14 2021

@author: 91799
"""
#Empty class
class account:
    pass
myobj=account()
print(myobj)

#self parameter
class myBuild():
    def mymethod(self, a=10, b=20):
        c=a+b
        print("Hello")
        print("welcome to the python world")
        return c
myobj = myBuild()
print(myobj.mymethod())

#constructor

class defCons():
    def __init__(self, name):
        self.name=name
    def myName(self):
        print("My Name is :", self.name)
        return
myobj = defCons("subhani")
print(myobj.myName())
