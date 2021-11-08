# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:46:49 2020

@author: 91799
"""

word_list = ["percussion", "supersonic", "car", "tree", "boy", "girl", "arc"]
anagram_list = []
for word_1 in word_list: 
    for word_2 in word_list: 
        if word_1 != word_2 and (sorted(word_1) == sorted(word_2)):
            anagram_list.append(word_1)
print(anagram_list)


arr = ['cat', 'dog', 'tac', 'god', 'act']
arr_list = []
for arr_1 in arr:
    for arr_2 in arr:
        if arr_1 != arr_2 and sorted(arr_1)==sorted(arr_2):
            arr_list.append(arr_1)
            print(arr_list)

from collections import Counter
word = ['d', 'a', 'b', 'a', 'b']
print(Counter(word))


from itertools import groupby
strings = ["apple", "orange", "grapes", "pear", "peach"]
print([list(g) for k,g in groupby(sorted(strings, key=sorted), sorted)])

a_list = [[1,2,3,4],"a","b","c",[11,12,13,14,15]]

total=0
a=[10,20,30,40,50]
for i in range(0, len(a)):
    if i==len(a)-1:
        print('er',i)

a_list = [[1,2,3,4],"a","b","c",[11,12,13,14,15]]
for a in a_list:
    print(a)
        


