# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:28:08 2020

@author: 91799
"""

import xlrd
filename='C:/Users/91799/Desktop/Demo.xlsx'
workbook=xlrd.open_workbook(filename)
sheet=workbook.sheet_names()
print(sheet)
data=[]
for sheet_names in sheet:
    sh=workbook.sheet_by_name(sheet_names)
    print(sh)
    for nrow in range(sh.nrows):
        print(nrow)
        nvalues=sh.row_values(nrow)
        print(nvalues)
        data.append(nvalues[0])
        print(data)

a=[3,6,9,12,15]
b=[]
for i in range(0, len(a)):
    b.append(a[i])
    print(b[i])
    if(b[i]==max(a)):
        b.append(a[i]+3)
        print(b)
a=[2,4,6,8,10]
C=[]
for i in range(0, len(a)):
    C.append(a[i])
    if C[i]==max(a):
        C.append(a[i]+2)
        print(C)

New_list=[10,20,30,40]
New_list2=[]
for k in range(0, len(New_list)):
    New_list2.append(New_list[k])
    print(New_list2)
    if New_list2[k]==max(New_list):
        New_list2.append(New_list[k]+10)
        print(New_list2)

dictA={'A':[1,2,3], 'B':[4,5,6], 'c':[7,8,9]}
result = {}
for i,j in dictA.items():
    result[i]=sum(j)
    print(result[i])

A={k:sum(v) for k,v in dictA.items()}
print(A)

A={'one':[2,3,4], 'two':[5,6,7], 'three':[8,9,10]}
B={k:sum(v) for k,v in A.items()}
print(B)

DICTA={'A':[10,20], 'B':[30,40], 'C':[50,60]}
DICTB={k:sum(b) for k,b in DICTA.items()}
print(DICTB)
    