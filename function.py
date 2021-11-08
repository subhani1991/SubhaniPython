# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 16:07:27 2021

@author: 91799
"""
def greek():
    print("welcome")
    print("Hello world!!")
greek()


#argument function

def greek(name):
    print("Hello world!")
    print("How do you do?", name)
greek("subhani")

#multiple arguments pass

def add_numbers(n1, n2):
    result=n1+n2
    print("The sum is:", result)
    return result
n1=10
n2=20
add_numbers(n1, n2)


def add_numbers(n1, n2):
    result=n1+n2
    print("The sum is:", result)
    return result
number1=10
number2=20
result = add_numbers(n1, n2)
print(result)

def find_avg_marks (marks):
    sum_of_marks=sum(marks)
    total_subjects = len(marks)
    avg_of_marks=sum_of_marks/total_subjects
    print(avg_of_marks)
    return avg_of_marks
marks=[80,70,60,50,40]
avg_of_marks = find_avg_marks(marks)
print(avg_of_marks)

def find_avg_marks (marks):
    sum_of_marks=sum(marks)
    total_subjects = len(marks)
    avg_of_marks=sum_of_marks/total_subjects
    print(avg_of_marks)
    return avg_of_marks
def compute_grade(avg_of_marks):
    if avg_of_marks >= 80:
        grade=='A'
    elif avg_of_marks >=60:
        grade=='B'
    elif avg_of_marks >=50:
        grade =='C'
    else:
        grade =='D'
    return grade
marks = [90,80,70,60]
avg_of_marks = find_avg_marks(marks)
print(avg_of_marks)
grade = compute_grade(avg_of_marks)
print(grade)
