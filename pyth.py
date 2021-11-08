# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 09:33:48 2020

@author: 91799
"""

a=[1,2,3,4,5]
for i in a:
    b=[]
    b.append(i+1)
    print(b)

a=[1,2,3,4]
a[-1]=5
print(a)

total=0
a=[10,20,30,40,50]
for i in range(0, len(a)):
    if i==len(a)-1:
        print('er',i)

a='welcometothepythonworld'
print(a.split(","))

a=[10,20,30,40,50]
def fun(n):
    for n in a:
        print(n)
a='df djff dsfjsdjlf'
print(a.split(" "))

A='ABCDEFGHIJK'
B=A.lower()
print(B)
C=B.capitalize()
print(C.upper())
x=[]
a=[num**2 for num in x]
print(a)

def sqr(num):
    return num**2
output=sqr(5)
print(output)

mylist=[n**2 for n in range(5)]
print(mylist)

mydict={v:v*2 for v in range(10)}
print(mydict)
i=1
while i<5:
    i+=1
    print(i)
for x in range(0,5):
    print(x)


filename='C:/Users/91799/Desktop/Demo.xlsx'
import xlrd
workbook=xlrd.open_workbook(filename)
sheet=workbook.sheet_by_index(0)

col=sheet.ncols
print('col: ', col)
row=sheet.nrows
print('row', row)
for colms in range(col):
    print('colms',colms)
for rows in range(row):
    print('rows:', rows)
   
data=[[sheet.cell_value(r,c) for c in range(col) for r in range(row)]]
print('data: ', data)


import xlrd
workbook=xlrd.open_workbook(filename)
sheet=workbook.sheet_names()
print(sheet)
data=[]
for sheet_name in sheet:
    sh=workbook.sheet_by_name(sheet_name)
    for nrow in range(sh.nrows):
        print(nrow)
        row_value=sh.row_values(nrow)
        data.append(row_value[2])
        print("DATA :", data[0])