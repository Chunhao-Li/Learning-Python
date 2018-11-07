#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:40:08 2018

@author: u6527752
"""

global_X = 27

def my_function(param1=123, param2="hi mom"):
    global_X = 5
    local_X = 654.321
    print("\n=== local namespace ===")  # line 1
    for name,val in list(locals().items()):
        print("name:", name, "value:", val)
    print("=======================")
    print("local_X:", local_X)
    print("global_X:", global_X)  # line 2

my_function()
print(global_X)