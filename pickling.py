# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:12:56 2021

@author: 91799
"""
import pickle

def pickle_data():
    data = {
                'name': 'Prashant',
                'profession': 'Software Engineer',
                'country': 'India'
        }
    filename = 'PersonalInfo'
    outfile = open(filename, 'wb')
    pickle.dump(data,outfile)
    outfile.close()
    
pickle_data()

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }
filename = 'dogs'
outfile = open(filename,'wb')
pickle.dump(dogs_dict,outfile)
outfile.close()

infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()

print(new_dict)
print(new_dict==dogs_dict)
print(type(new_dict))


"""import pickle

def unpickling_data():
    file = open(filename,'rb')
    new_data = pickle.load(file)
    file.close()
    return new_data


print(unpickling_data())
"""