# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 12:06:49 2021

@author: 91799
"""


data_path = "C:\\Users\\91799\\pyspark"

nums = range(1, 30)


rdd1 = sc.parallelize(nums, 2)

print("rdd1 Partitions : {} ".format(rdd1.getNumPartitions()))

print("Partitioner : {} ".format(rdd1.partitioner))