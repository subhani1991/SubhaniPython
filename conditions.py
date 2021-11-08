# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 19:59:34 2020

@author: 91799
"""

a=['subhani', 'python', 'shaik', 'subhani']
for lst in a:
    print("test",lst)
    if(lst =='python'):
        print("lst : ", lst)
        print(True)
        continue
    
    else:
        print(False)
        
lst=['I', 'am', 'Python', 'Programmer']

s=""
for x in lst:
    s+=x
    s="".join(lst)
    print(s)
    
class A(object):
    def __repr__(self):
        return "instant of A"

a=A()
b=a
del a
print(b)

import copy
class A(object):
    pass
a=A()
a.lst=[1,2,3]
a.str='cats and dogs'
b=copy.copy(a)
a.lst.append(100)
a.str = 'cats and mice'
print(b.lst)
print(b.str)


a=['orange', 'apple', 'banana']
b=a
a=['tomato', 'cucumber', 'carrot']
print(b)



import datetime
class Human(object):
    name=None
    gender=None
    birthdate=None
    def __getattr__(self, name):
        if name == 'age':
            return dattime.datetime.now()-self.birthdate
        else:
            return None
    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
h=Human()
h.birthdate=datetime.datetime(1984,8,20)
h.age=28
print(h.age) 

l=[i for i in range(10000)]  
x=[i for i in range(10000)] 
print(l)
print(s)


class  A:
    brothers=[]
    def __init__(self, name):
        self.name=name
a=A('Richard')
b=A('Eilly')
a.brothers.append('john')
print(a.name,a.brothers,b.name,b.brothers)
    