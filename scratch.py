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

def walk(dirname):
    """Finds the names of all files in dirname and its subdirectories.
    dirname: string name of directory"""
    names = []
    if '__pycache__' in dirname:
        return names
    
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        
        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names

def compute_checksum(filename):
    """Computes the MD5 checksum of the contents of a file.
    filename: string"""
    cmd = 'md5sum ' + filename
    return pipe(cmd)

def check_diff(name1, name2):
    """Computes the difference between the contents of two files.
    name1, name2: string filenames
    """
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)

def pipe(cmd):
    """ Runs a command in a subprocess.
    cmd: string Unix command
    Returns (res, stat), the output of the subprocess and the exit status.
    """
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat

def fibonacci1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)
    
known = {0:0, 1:1}

def fibonacci2(n):
    if n in known:
        return known[n]
    
    res = fibonacci2(n-1) + fibonacci2(n-2)
    known[n] = res
    return res