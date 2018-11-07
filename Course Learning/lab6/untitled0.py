#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:15:31 2018

@author: u6527752
"""

import csv
with open("daily-max-temp-CBR.csv") as csvfile:
    reader = csv.reader(csvfile)
    table1 = [ row for row in reader ]
with open("daily-min-temp-CBR.csv") as csvfile:
    reader = csv.reader(csvfile)
    table2= [ row for row in reader ]
    
def sub_zero_ls(t2):
    del t2[0]
    num_col5 = [[int(row[2]), int(row[3]),float(row[5])] for row in t2 if row[5] != '']
    sub_zero = [row for row in num_col5 if row[2] <0 ]
    return sub_zero
 
def count_s_z_nights(y,ls):
    sub_zero = sub_zero_ls(ls)
    specific_y = [row for row in sub_zero if row[0] == y and (row[1] in [6,7,8])]
    return len(specific_y)

def funA(alist):
    if len(alist)==0:
        return alist
    else:
        return funA(alist[1:]) + [alist[0]]
    
def funB(alist):
    if len(alist) > 0:
        x= alist.pop(-1)
        alist = funB(alist)
        alist.insert(0,x)
    return alist

def make_list_of_lists(n):
    the_list = []
    sublist = []
    while n > 0:
        the_list.append(sublist[:])
        sublist.append(len(sublist) + 1)
        n = n - 1
    return the_list


def make_list_of_lists1(n):
    the_list = []
    sublist = []
    for i in range(1,n+1):
        the_list.append(sublist[:])
        sublist.insert(len(sublist), i)
    return the_list

i = 0

def find_max(seq):
    global i
    if i == len(seq) - 1:
        return seq[-1]
    else:
        first = seq[i]
        i = i + 1
        max_of_rest = find_max(seq)
        return max(first, max_of_rest)
    
def allbut(a_list, index):
    new_ls = []
    for i in range(len(a_list)):
        if i != index:
            new_ls.append(a_list[i])
        else:
            pass
    return new_ls

def slice_in_place(a_list, start, end):
    for i in sorted(range(len(a_list)), reverse = True):
        if i not in range(start%4,end%4):
            a_list.pop(i)
