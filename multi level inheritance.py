# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:58:58 2021

@author: 91799
"""
class person():
    def printMe(self):
        print("i am a main base class")
class employee(person):
    def display(self):
        print("i am employee class")
class programmer(employee):
    def show(self):
        print("i am programmer class")
myprog=person()
print(myprog.printMe())
myobj1=employee()
print(myobj1.display())
myobj2=programmer()
print(myobj2.show())

a=['a','b','c','d']
print(a[0:1])
x=10
y=x
x=5
print(y)
l1=[1,2,3,4]
l2=[1,2,3]
l3=l2
print(l2 is l3)

a=[]