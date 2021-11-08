# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:01:56 2021

@author: 91799
"""
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

#shallow copy

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)

#adding nested objects in shallow copy
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)

#Deep copy

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3],[5,5,5]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3],[4,4,4]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)