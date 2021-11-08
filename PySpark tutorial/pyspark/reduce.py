# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:47:49 2021

@author: 91799
"""

from operator import add

out1 = sc.parallelize([1,2,3,4]).reduce(add)
print(out1)


out2 = sc.parallelize((2 for _ in range(10))).map(lambda x: x*x).cache().reduce(add)
print("OUTPUT2 : " , out2)