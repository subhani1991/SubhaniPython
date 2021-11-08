# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:19:42 2020

@author: 91799
"""


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1
sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)

index = [1,2,3,4,5]
print(index[0], index[4])

doubles = [2+ n for n in range(50)]
print(doubles)

my_list = [1,2,3,4,5]
gen = (x**2 for x in my_list)
print(gen.__next__())
print(gen.__next__())
print(next(gen))

a=[1,2,3,4]
b=[5,6,7,8]
a.append(b)
print(a)
c=a+b
print(c)

from past.builtins import xrange
for i in xrange(10):
    print(i)
    
class test:
        def init_(self):
        self.variable = 'Old'
        self.Change(self.variable)
    def Change(self, var)
        var = 'New'
obj=test()
print(obj.variable)
