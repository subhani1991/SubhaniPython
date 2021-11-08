# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:56:48 2021

@author: 91799
"""
a=[1,3,5,7,9,2,4,6,8]
print(a)
b=(1,3,5,6,7,8,9,2)
print(b)
Tt=(1,2,(30,40))
print(hash(Tt))

#append
my_a_list=[1,2,3,4,5]
my_a_list.append([1,2,4])
print(my_a_list)
my_a_list.extend([1,2,3])
print(my_a_list)
my_main_list=[1,2,3,4,5,6,7,8,9,10]
my_main_list[0:]
print(my_main_list)

my_string_slice="subhani shaik honey"
print(len(my_string_slice))
print(my_string_slice[0:8:2])
print(my_string_slice[:-2])

a=[1,2,3,4,5,6,7,8,9]
print(a.pop(8))
a.remove(6)
print(a)

#Insert
my_insert_list=['a', 'b', 'c', 1, 2]
my_insert_list[1]='subhani'
print(my_insert_list)

#Count
my_count_list=[1,2,3,4,[5,6,7],(8,9,10)]
print(my_count_list.count(4))
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
# List Reverse
systems.reverse()
# updated list
print('Updated List:', systems)

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list	
# Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]


# updated list
print('Updated List:', reversed_list)
a=[1,2,3]
b=a
c=[1,2,3,4]
print(b is a)
print(a is b)
print(a is c)

#packing & unpacking

x=("subhani", "30yrs", "pamur")
(name, age, place_of_birth)=x
print(name)
print(age)
print(place_of_birth)
