#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:02:55 2018

@author: u6527752
"""

#Function 1
def any_one_is_sum(a,b,c):
    sum_c=a+b
    sum_b=a+c
    sum_a=b+c
    if sum_c == c or sum_b == b or sum_a == a:
          return True
    else:
        return False
#Function 2
def any_one_is_sum2(a,b,c):
    if b + c == a:
        return True
    elif a + c == b:
       return True
    elif a + b == c: 
        return True
    else:
        return False
 
def any_one_is_sum21(a,b,c):
    if b + c == a:
       print(True)
    elif a + c == b:
       print(True)
    elif a + b == c: 
        print(True)
    else:
        print(False)
     
#Function 3
def any_one_is_sum3(a, b, c):
    if a+b==c or a+c==b or b+c==a:
        return True
    else:
        return False


#Exercise 1    
#Function 1
def integrate(lower, upper, nterms):
    # divide the interval into nterms even-sized parts
    delta = (upper - lower) / nterms
    total = 0
    while lower+delta >= upper:
        # compute area from lower to lower + delta
        area = ((1/lower) + (1/(lower + delta))) * delta / 2
        print(area)
	# add to total area
        total = total + area
        lower = lower + delta
    return total
#Function 2
def integrate1(lower, upper, nterms):
    # divide the interval into nterms even-sized parts
    delta = (upper - lower) / nterms
    total = 0
    while lower < upper:
        # compute area from lower to lower + delta
        area = ((1/lower) + (1/(lower + delta))) * delta / 2
        print (area)
	# add to total area
        total = total + area
        delta = (upper - lower) / nterms
        lower = lower + delta


#Exercise 3        
def average(numbers):
    total = 0
    index = 0
    while index < len(numbers):
        total = total + numbers[index]
        index = index + 1
    return total / len(numbers)

def new_average(numbers):
    return sum(numbers)/len(numbers)

def most_average(numbers):
    ab = float('inf') 
    for x in numbers:
        current_abs = abs(x-new_average(numbers))
        if current_abs <= ab:
            ab = current_abs
            current_num = x
    return current_num    
    
#Exercise 3(c)
def count_negative(numbers):
    current_c = 0
    for x in numbers:
        if x < 0:
            current_c = current_c +1
    return current_c

#Exercise 4
#Function 1
def is_increasing(seq):
    i = 0
    while i < len(seq)-1:
       if seq[i + 1] < seq[i]:
           return False
       i = i + 1
    return True
#Function 2
def is_increasing2(seq):
    i = len(seq) - 1 
    while i > 0:
       if seq[i] < seq[i - 1]:
           return False
       i = i - 1
    return True

#Exercise 5
def n_element(a,n):
     return [a]*n
 
def step_ls(n,k):
    return list(range(-n,n+1,k))

def index_ls(n):
    return list(range(1,n))

#Lab 5
    
#Exercise 3
def count_negative2(array):
    count=0
    for elem in array:
        if elem < 0:
            count += 1
    return count

def count_capitals(string):
    count = 0
    for char in string:
        if 65<=ord(char)<=90:
            count += 1
    return count

def count(seq,fun):
    count=0
    for elem in seq:
        if fun(elem) == True:
            count += 1
    return count
    
def is_negative(a):
    if a<0:
        return True
    else:
        return False
    

            
    