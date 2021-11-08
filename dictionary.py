# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:11:39 2020

@author: 91799
"""

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}  
print("Dictionary:")  
print(Dict) 
print(Dict[1])

from collections import defaultdict 

def def_value(): 
    return "Not Present"

d = defaultdict(def_value) 
d["a"] = 1
d["b"] = 2
  
print(d["a"]) 
print(d["b"]) 
print(d["c"]) 

d = defaultdict(list) 
  
for i in range(5): 
    d[i].append(i) 
      
print("Dictionary with values as list:") 
print(d)

d = defaultdict(int) 
   
L = [1, 2, 3, 4, 2, 4, 1, 2] 
for i in L:
    d[i] += 1
print(d)
