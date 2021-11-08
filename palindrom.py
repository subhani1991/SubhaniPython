# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:20:45 2020

@author: 91799
"""

n=15
temp=n
rev = 0
while(n>0):
    dig = n%10
    print(dig)
    rev = rev*10+dig
    print(rev)
    n=n//10
    print(n)
    if(temp==rev):
        print("this is polindrome number: ,")
    else:
        print("not a polindrome number:,")

x="malayalam"
y = ''
for i in x:
    y = i+y
    if(x==y):
        print("s")
    else:
        print("No")

def isPalindrome(s):
    rev = ''.join(reversed(s))
    if(s==rev):
        return True
    else:
        return False
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("S")
else:
    print("NNN")