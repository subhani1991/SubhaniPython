# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 21:51:16 2021

@author: 91799
"""
#generating unit test case

# unit test case
'''
import unittest

class TestStringMethods(unittest.TestCase):
	# test function to test equality of two value
	def test_positive(self):
		firstValue = "geeks"
		secondValue = "geeks"
		# error message in case if test case got failed
		message = "First value and second value are not equal !"
		# assertEqual() to check equality of first & second value
		self.assertEqual(firstValue, secondValue, message)

if __name__ == '__main__':
	unittest.main()
    '''


'''
class my_test_case(unittest.TestCase):
    def my_function(self):
        first_name = "subhani"
        last_name = "shaik"
        full_name = first_name + last_name
        self.assertRaises(first_name, last_name, full_name)

class my_test_case_1(unittest.TestCase):
    def my_name(self):
        username = "welcome"
        print("USERNAME : ", username)
        self.assertEqual(username)
        
class my_test_case_2(unittest.TestCase):
    def add(self, username):
        username  = "subhani"
        if len(username)>3:
            self.assertEqual(username)  
            '''
def add(x,y):
    print("print the adding of two elements:")
    
    return x+y
#print(add(5,10))

def sub(a,b):
    return a-b
#print(sub(30,20))

def mul(c,d):
    return c*d
#print(mul(10,20))

def div(a,b):
    if b==0:
        raise ValueError("can not be divided by zero")
    return a/b
#print(div(8,2))

class myTest(unittest.TestCase):
    def calc(self):
        result = add(10,20)
        print("result : ", result)
        self.assertEqual(result, 0)
        



  