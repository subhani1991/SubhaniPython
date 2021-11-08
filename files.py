# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 10:46:30 2019

@author: 91799
"""
'''

with open("C:/Users/91799/Desktop/test.txt", mode='r') as myfile:
    f=myfile.read(4)
    print(f)
    



f=open("C:/Users/91799/Desktop/new.txt", "r")
data=f.read()
for lines in data:
    print(lines)
    

line_nuber=2    
fo = open("C:/Users/91799/Desktop/new.txt", "r")
current_line=1
for line in fo:
    if(current_line == line_nuber):
        print(line)
        break
    current_line +=1
    print("TEST : ", current_line)


line_number=2
filename=("C:/Users/91799/Desktop/new.txt")
fo= open(filename, "r")
cur_line=1
for line in fo:
    if (cur_line == line_number):
        print(line)
        cur_line +=1
        print(cur_line)


with open(filename, 'r') as myfile:
    print(myfile.readlines())

file_1=open(filename, "w")
file_1.write("shaik subhani")
file_1.write("patan subhani")
'''
filename=("C:/Users/91799/Desktop/test.txt")
with open(filename, "w") as f:
    f.write("shaiksubhanishaik\n")
    f.write("erhgerhgh")


lines=["subhani\n", "shaik\n", "patan\n", "pytohn\n", "jfhsdhfkfhhfk"]
f=open("C:/Users/91799/Desktop/test.txt", "a+")
f.writelines(lines)
f.writelines(lines)
f.close()



    
