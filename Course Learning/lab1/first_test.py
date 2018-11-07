#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:15:15 2018

@author: u6527752
"""

import robot

def swap_left_and_middle():
    robot.drive_right()
    robot.lift_up()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_right()
    robot.drive_right()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.drive_left()
    robot.drive_left()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    robot.drive_right()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_open()


def swap_middle_and_right():
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_right()
    robot.drive_right()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_left()
    robot.drive_left()
    robot.lift_down()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    robot.drive_right()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_open()
    
def swap_left_and_right():
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_left()
    robot.drive_left()
    robot.drive_left()
    robot.drive_left()
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_right()
    robot.drive_right()
    robot.drive_right()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()
    robot.drive_left()
    robot.drive_left()
    robot.drive_left()
    robot.drive_left()
    robot.lift_down()
    robot.gripper_to_open() 

robot.init()
swap_left_and_middle()
swap_middle_and_right()
swap_left_and_right()