# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a="subhani"
if len(a)<=3:
    print(a)
else:
    print({"error":"error message"})
    
    
a=[10,20,30,40,50]
for i in a:
    if i%2==0 and i%3!=0:
        print("welcome: ", i)
    else:
        print("Boom")

a=10
b=a
print (a)
print (b)

names="youthtube"
print(names)
a=names[1]
print (a)
print(names[0])
print(names[0:9:2])
print (names[0:9:3])
print (names[0:9:4])
print(names[0:9:5])
print(names[0:9:6])
print(names[0:9:7])
print(names[0:9:8])
print(names[0:9:9])
print(names[0:])
print(names[:1])
print(names[0:3])
print(names[3:])
print(names[-1])
print(names[-2:])
print(names[:-2])
print(names[-3:])
print(names[:-3])
print(names[-4])
print(names[-4:])
print(names[:-4])
print(names[-5])
print(names[-5:])
print(names[:-5])
print(names[-6])
print(names[-6:])
print(names[:-6])
print(names[-7])
print(names[-7:])
print(names[:-7])

list_1 = [10,20,30,40,50,60]
print(len(list_1))
print(list_1[0])
print(list_1[1])
print(list_1[2])
print(list_1[3])
print(list_1[4])
print(list_1[5])
print(list_1[-5:])
print(list_1[:-5])
print(list_1[3:])
print(list_1[:3])
print(list_1[-3:])
print(list_1[:-3])

a=[10,20,30,40]
b=[50,60]
a.append(b)
a.extend(b)
print("c : ", a)

names=['navin', 'kiran', 'john']
values=[9.5, 'navin',25]
mil=[names, values]
print(mil)
print(mil[0])
print(mil[1])
print(mil[0][-1][:-1])
print(mil[1][-2][-3:-1])

#adding

nums=[29,12,14,36]
print(nums)
nums.extend([16,14])
print(nums)
