#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 07:42:34 2018

@author: frederick
"""

def count_ne_lines(path):
    file = open(path, 'r')
    count_num = 0
    for line in file:
       if line != '\n':
        count_num +=1
    file.close()
    return count_num

def p_reverse_file1(path):
    file = open(path)
    pos_ls = []
    while file.readline() != '':
        pos_ls.append(file.tell())
        file.readline()
    for pos in pos_ls[::-1]:
        file.seek(pos)
        line = file.readline()
        print(line)
    file.close()
    
def p_reverse_file2(path):
    file = open(path)
    line_ls = []
    while file.readline() != '':
        new_l = file.readline()
        line_ls.append(new_l)
    for line in reversed(line_ls):
        print(line)
    file.close()

import os
def list_all_files(dirname):
    ls = os.listdir(dirname)
    for elem in ls:
        if os.path.isdir(elem):
            ls.remove(elem)
            ls.extend(list_all_files(elem))
    return ls
            