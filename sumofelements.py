# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:25:25 2020

@author: 91799
"""

total = 0
list1 = [11, 5 ,17, 18 , 23]
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("sum of the all elements : ", total)


list1 = [11, 5 ,17, 18 , 23]
print(sum(list1))


l = [1000,298,3579,100,200,-45,900] 
n = 4
  
l.sort() 
print(l[-n:]) 

def Nmaxelements(list1, N): 
    final_list = [] 
  
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        final_list.append(max1) 
          
    print(final_list) 
  
# Driver code 
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10] 
N = 2
  
# Calling the function 
Nmaxelements(list1, N)

list1 = [10, 20, 4, 45, 99]
list2 = sorted(list1)
print(list2[-2])

list1 = [10, 20, 4, 45, 99] 
list2=sorted(list1)
print(list2[0])

list1 = [10, 20, 1, 45, 99] 
list2 = ("A : ", sorted(list1))
print(list2[-2])
list1 = [11, 5 ,17, 18 , 23]
list2=set(list1)
print(max(list2))


