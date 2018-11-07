#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 11:16:29 2018

@author: u6527752
"""

# distance voyager 1 & the Sun 21,259,598,000 km
#speed of voyager 1 16.9995 km/ second
# speed of radio waves = speed of light = 299,792,458 m/second
# current radio round trip time 141828 seconds

#distance = distance at start + velocity * time since start
#distance earth sun = 149,598,000 km

distance_start = 21259598000*1000 + 149598000*1000
time_input = input ("Enter a time: (days)")
velocity_time = float (time_input)

