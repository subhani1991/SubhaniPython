# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 12:06:49 2021

@author: 91799
"""
import os

data_path = "C:\\Users\\91799\\pyspark"

dirPath = os.path.join(data_path, "files")
os.mkdir(dirPath)

with open(os.path.join(dirPath, "2.txt"), "w") as file1:
    _ = file1.write("welcome to Python and Azure with Azure Cloud platformmakdcsd,fmncsmdfnvlxnlcnbc,bmdcb")
    

with open(os.path.join(dirPath, "2.txt"), "w") as file3:
    _ = file1.write("sdbmbfvcdfxghxkfhvbxvbdkfhxdshdfkhsdfcsdfbsdfsdfbsbdfhbsdhfgjsdbcjscjshgdjcsdbcvjdfgeyxfycheyreyteruyt3ueyrfkeht93uyherhgkdhhdgfgh")

textFiles = sc.wholeTextFiles(dirPath)    