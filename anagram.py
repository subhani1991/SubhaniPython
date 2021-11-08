# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:01:10 2020

@author: 91799
"""

list_1 = ["eat", "tea", "tan", "ate", "nat", "bat", "bats"]
list_2 = []

for word_1 in list_1:
    for word_2 in list_1:
        if word_1 != word_2:
            (sorted(word_1)==sorted(word_2))
            list_2.append(word_1)
            print(list_2)


from itertools import groupby

words = ['oog', 'abc', 'cab', 'cafe', 'face', 'goo', 'foo']

print ([list(g) for k, g in groupby(sorted(words, key=sorted), sorted)])

def check(s1, s2):
    if(sorted(s1)==sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

s1 ="listen"
s2 ="silent" 
check(s1, s2)

def allAnagram(input):
    dict = {}
    for strVal in input:
        key = ''.join(sorted(strVal))
        if key in dict.keys(): 
            dict[key].append(strVal) 
        else: 
            dict[key] = [] 
            dict[key].append(strVal)
    output = "" 
    for key,value in dict.items(): 
        output = output + ' '.join(value) + ' '
    
    return output
if __name__ == "__main__": 
    input=['cat', 'dog', 'tac', 'god', 'act'] 
    print (allAnagram(input))

from collections import defaultdict

test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum'] 
print("The original list : " + str(test_list))
temp = defaultdict(list)
for ele in test_list:
    temp[str(sorted(ele))].append(ele)
res = list(temp.values())
print("The grouped Anagrams : " + str(res)) 

from itertools import groupby 
test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum']
temp = lambda test_list: sorted(test_list)
print(temp)
res = [list(val) for key, val in groupby(sorted(test_list, key = temp), temp)] 
print(str(res))

from collections import Counter
def removeChars(str1, str2):
    dict1=Counter(str1)
    dict2=Counter(str2)
    keys1 = dict1.keys()
    keys2=dict2.keys()
    count1 = len(keys1)
    count2 = len(keys2)
    set1 = set(keys1)
    commonKeys = len(set1.intersection(keys2))
    if(commonKeys == 0):
        return count1 + count2
    else:
        return (max(count1, count2)-commonKeys)
if __name__ == "__main__":
    str1 = 'bcadeh'
    str2 = 'hea'
    print(removeChars(str1, str2))


l = [8,10,4,5,7]
filterl = [a for a in l if a % 2 != 0]
print(filterl)
    
    

        
