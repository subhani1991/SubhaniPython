# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 09:52:14 2021

@author: 91799
"""
import findspark

findspark.init()

import os
from pyspark import SparkContext

data_path="C:\\Users\\91799\\pyspark"

sc=SparkContext("local", "map")

rdd_data=sc.parallelize([1,2,3,4])

rdd_map_1 = rdd_data.map(lambda x:[x,x,x])
for x in rdd_map_1.collect():
    
    print(x)


sc.stop()