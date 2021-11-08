# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:28:57 2021

@author: 91799
"""
rdd=sc.parallelize(range(0,10))

rdd1 = sc.parallelize(
    [
     ("python",12),
     ("PySpark",12),
     ("Hadoop",12),
     ("python",12), 
     ("PySpark",1),
     ("python",1)
     ]
    )
out1=sorted(rdd1.countByKey().items())

out2=sorted(rdd1.countByValue().items())

#Count By Key
print("COUNTBYKEY: ",out1)

#count By Value
print("COUNTBYVALUE : ",out2)