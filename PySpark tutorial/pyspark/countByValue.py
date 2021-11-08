# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:34:40 2021

@author: 91799
"""

rdd=sc.parallelize(range(0,10))

rdd = sc.parallelize(
    [
     ("python",1),
     ("pyspark",1),
     ("spark",1),
     ("Hadoop",1),
     ("python",1),
     ("pyspark",1),
     ("spark",1)
     ]
    )
out1=sorted(rdd.countByValue().items())
print("OUTPUT1",out1)

rdd2=sc.parallelize([1,2,2,2,3,4,5,6,3,6,7,8,4,6,3,7,4,5,6,8,9,10,3])
out2=sorted(rdd2.countByValue().items())
print("OUTPUT2",out2)