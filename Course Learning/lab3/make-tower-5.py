
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

# main program

robot.init(width = 9, boxes = "flat")

# position above first box
robot.drive_right()
robot.lift_up()

# pick up, move right
pickup_next()
move_to_next_stack()

# ...again
pickup_next()
move_to_next_stack()

# ...again
pickup_next()
move_to_next_stack()

# ...again
pickup_next()
move_to_next_stack()

# tower is done, park the robot
robot.gripper_to_folded()
robot.lift_down()
