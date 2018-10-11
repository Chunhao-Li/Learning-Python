#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 00:45:16 2018

@author: frederick
"""

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


if __name__ == '__main__':  
    print(linecount('wc.py'))