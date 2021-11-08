# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 16:50:03 2021

@author: 91799
"""
def even_generator():
    n=0
    n+=2
    yield n
    n+=2
    yield n
    n+=2
    yield n
numbers=even_generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))

def even_num(max):
    n=2
    
    while n<=max:
        yield n
        n+=2
        
numbers = even_num(4)
print(next(numbers))
print(next(numbers))


#fibonacci

def generate_fibonacci():
    n1=0
    n2=1
    while True:
        yield n1
        
        n1, n2 = n2, n1+n2
seq = generate_fibonacci()

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))

#even numbers
def all_even():
    n=0
    while True:
        yield n
        n+=2
seq1=all_even()
print("even:", next(seq1))
print(next(seq1))
print(next(seq1))
print(next(seq1))
print(next(seq1))
print(next(seq1))

#odd numbers
def all_even():
    n=0
    while True:
        yield n
        n+=2
seq1=all_even()
print("even:", next(seq1))
print(next(seq1))
print(next(seq1))
print(next(seq1))
print(next(seq1))
print(next(seq1))


my_list = [1, 3, 6, 10]
a=(x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

my_list = [1,3,6,10]
list_ = [x**2 for x in my_list]
generator = (x**2 for x in my_list)

print(list_)
print(generator)

#reverse string
def rev_str(my_str):
    length = len(my_str)
    
    for i in range(length-1, -1, -1):
        yield my_str[i]
        
for char in rev_str("subhani"):
    print(char)
        
        


















