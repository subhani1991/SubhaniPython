# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:59:56 2020

@author: 91799
"""

mytuple = ["apple", "banana", "cherry"]
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

b={1,2,3,4}
a=iter(b)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


from itertools import count
sequence = count(start=1, step=3)
while(next(sequence)<=10):
    print(next(sequence))

list =['python', 'flask', 'django', 'hadoop']
for word in list:
    print(len(list))
    print(word)
