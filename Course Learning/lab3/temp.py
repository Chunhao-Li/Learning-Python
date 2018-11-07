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
              
    else:
        0<=mark<50
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

import robot

def move_to_next_stack():
    '''move robot two steps right'''
    robot.drive_right()
    robot.drive_right()

def pickup_next():
    '''Release the box in gripper (if any) and pick up the one below.
    Assumption: robot is in front of a box/stack; lift is at level 1.'''
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()

def make_tower(n):
    robot.init(width = 2*n-1, boxes = "flat")
    robot.drive_right()
    robot.lift_up()
    while n>1:
        pickup_next() 
        move_to_next_stack()
        n=n-1
    robot.gripper_to_folded()
    robot.lift_down()


def find(colour):
    current_hight=0
    current_color = robot.sense_color()
    while current_color != '':
        while current_color != colour:
            robot.lift_up()
            current_hight=current_hight+1
            current_color = robot.sense_color()
            if current_color == '':
                return -1
        else:
            current_color == colour
            return current_hight, current_color
 

    

