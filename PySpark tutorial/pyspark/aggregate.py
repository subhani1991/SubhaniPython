# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:15:04 2021

@author: 91799
"""

seqOp = (lambda x,y:(x[0]+y, x[1]+1))
combOp = (lambda x,y:(x[0]+y[0], x[1]+y[1]))

rdd1=sc.parallelize([1,2,3,4,5,6,7,8,9,10],2)
sumcount = rdd1.aggregate((0,0), seqOp, combOp)
print("sumcount : ", sumcount)