#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:31:38 2018

@author: frederick
"""

def max_increase(seq):
    increase = []
    for i in range(len(seq)):
        increase.append(max(seq[i:])-seq[i])
    return max(increase)