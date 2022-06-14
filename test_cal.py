# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 21:51:16 2021

@author: 91799
"""
#generating unit test case

# unit test case

import unittest

import calc

class testCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,20), 30)
        
        

if __name__ == "__main__":
    unittest.main()
     



  