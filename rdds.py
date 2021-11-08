# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:31:20 2021

@author: 91799
"""
import findspark
findspark.init()
from pyspark import SparkContext

sc = SparkContext("local", "data")

filepath="E:\\Morrison\\data.csv"