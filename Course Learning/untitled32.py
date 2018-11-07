#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:40:19 2018

@author: frederick
"""

def individual_risk(x, y, vegetation_type, vegetation_density):
    
#    a = 0.2 Shrubland Pine Forest
#    a = 0.1 Arboretum
#    a = 0.05 Urban Vegetation Golf Course
    
    if vegetation_density[x][y] == "":
        return 0
    
    if vegetation_type[x][y] == "Shrubland" or vegetation_type[x][y] == "Pine Forest":
        a = 0.2
    
    elif vegetation_type[x][y] == "Arboretum":
        a = 0.1
        
    elif vegetation_type[x][y] == "Urban Vegetation" or vegetation_type[x][y] == "Golf Course":
        
        a = 0.05
    
    else:
        
        a = 0
        
    return math.sqrt(a + float(vegetation_density[x][y]))

def check_edge(values):
    
    if values < 0:
        values = 0
    
    if values > 149:
        values = 149
        
    return values
    

def fire_risk(x, y, vegetation_type, vegetation_density, wind_speed):
    
    if wind_speed[x][y] != '':
        n = int(float(wind_speed[x][y]))
    if wind_speed[x][y] == 0 or wind_speed[x][y] == '' :
        return individual_risk(x, y, vegetation_type, vegetation_density)
    #self_risk = individual_risk(x, y, vegetation_type, vegetation_density)
    
    x_min = check_edge(x-n)
    x_max = check_edge(x+n)

    y_min = check_edge(y-n)
    y_max = check_edge(y+n)
    risks = 0
    for i in range(x_min,x_max+1):
        for j in range(y_min,y_max+1):
            
            risks+= individual_risk(i, j, vegetation_type, vegetation_density)
    return risks