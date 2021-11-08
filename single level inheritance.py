# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:46:55 2021

@author: 91799
"""
''''
syntax for single level
class Base Class:
    Body of the Base class
class derived class(Base class):
    Body of the derived class
'''
class Animal:
    def dog(self):
        print("eating")
class Fox(Animal):
    def sound(self):
        print("Barking")
myobj1 = Animal()
myobj2=Fox()
print(myobj1.dog())
print(myobj2.sound())