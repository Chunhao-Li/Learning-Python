# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def print_grade(mark):
    while 100>=mark >= 80:
        print("High Distinction")
        break
    while 80>mark >= 70:
        print("Distinction")
        break
    while 70>mark >= 60:
        print("Credit")
        break
    while 60>mark >= 50:
        print("Pass")
        break      
    while 0<=mark<50:
        print("Fail")
        break
    
    

def print_grade_elif(mark):
    if 100>=mark >= 80:
        print("High Distinction")
        
    elif 80>mark >= 70:
        print("Distinction")
        
    elif 70>mark >= 60:
        print("Credit")
        
    elif 60>mark >= 50:
        print("Pass")
              
    elif 0<=mark<50:
        print("Fail")
 
def median(a,b,c):
   
    if a<=b:
        if b<=c:
            return b
        elif c<=a:
            return a
        else:
            return c
    else:
        if c<=b:
            return b
        elif c>=a:
            return a
        else: 
            return c
        

def mystery(m):
    while m > 1:
        i = 2
        while i < m:
            while m % i == 0:
                m = m // i
            i = i + 1
    return i