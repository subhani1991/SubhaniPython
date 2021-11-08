# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:50:42 2020

@author: 91799
"""


import xlrd
filename="C:/Users/91799/Desktop/Book-1.xlsx"
workbook=xlrd.open_workbook(filename)
sheet=workbook.sheet_by_index(0)
print(sheet)
data=[]
col=sheet.ncols
print(col)
row=sheet.nrows
print(row)
for ncols in range(col):
    print(ncols)
for nrows in range(row):
    print(nrows)


workbook=xlrd.open_workbook(filename)
sheet_name=workbook.sheet_names()
print(sheet_name)

sh=workbook.sheet_by_name(sheet_name[0])
print(str(sh))
sh_row=sh.row(0)
print(sh_row)
sh_col=sh.col(0)
print(sh_col)

row = sh.row(0)
print(row)
col=sh.col(2)
print(col)


import pandas as pd
df=pd.read_excel(filename)
print(df)

df1=pd.DataFrame(df)
print(df1['USERNAME'][3])


Fname="C:/Users/91799/Desktop/python123.txt"
f=open(Fname, 'r')
lines=0
words=0
characters=0
for line in f:
    wordsList=line.split()
    print("w : {}".format(wordsList))
    characters+=len(line)
    lines+=1
    words+=len(wordsList)
    print("LINES {}".format(lines))
    print("words {}".format(words))
    print("characters {}".format(characters))

a="\\subhani\\shaik\\"
print(a)

list_1=['a', 'b', 'c', 'd']
"".join(list_1)
print(list_1)

st="subhanishaik"
st.split()
print(st)
s1=[1,4,6,8,2,3]
s1.sort()
print(s1)
A=['bcadfeg']
print(A.sort())

a='abcde'
a.lower()
print(a.capitalize())
print(a.count('abc'))

import random
word = list('abracadabra')
random.shuffle(word)
print(word)

my_list=[0,1,2,3,4,5,6,7,8,9]
b=len(my_list)
my_list.append(b)
print(my_list)


'''packing
'''
def add_num(a,b):
    result=a+b
    print(result)
a=add_num(5,10)
print(a)

'''
unpacking
'''
def sum_num(*args):
    print(args)
a=sum_num(2,3,4,5,6)
print(a)


a={'a':1, 'b':2, 'c':3, 'd':4, 'f':5, 'e':6}
b=sorted(a.items())
print(dict(b))

def my_fun(lst):
    for num in lst:
        yield num
result=my_fun([1,2,3,4,5])
print(list(result))
print(type(result))

