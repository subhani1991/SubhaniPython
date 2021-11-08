# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:53:37 2021

@author: 91799
"""

out1 = sc.parallelize([10, 1, 2, 9, 3, 4, 5, 6, 7]).takeOrdered(6)
print(out1)

out2 = sc.parallelize([10, 1, 2, 9, 3, 4, 5, 6, 7], 2).takeOrdered(6, key=lambda x: -x)
print("TAKEORDERED", out2)