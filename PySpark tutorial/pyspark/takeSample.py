# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:01:57 2021

@author: 91799
"""

rdd = sc.parallelize(range(0,10))

rdd.count()

sample1 = rdd.takeSample(True, 20, 1)
print("sample1 : ", sample1)

sample2 = rdd.takeSample(False, 5, 4)
print("sample2 : ", sample2)

sample3 = rdd.takeSample(False, 15, 3)
print("sample3 : ", sample3)