## COMP1730/6730 S2 2018 - Homework 3
# Submission is due 9am, Monday the 27th of August, 2018.

## YOUR ANU ID: u6527752
## YOUR NAME:Chunhao Li


## Modify the following function definitions so that they compute and
## return the correct answers to the homework problems. (The statement
## "return 1" is just a placeholder: you should of course modify it.)

def sum_odd_digits(number):
    '''Choose the odd numbers, then digit sum
    r_m : rightmost digit'''
    current_sum = 0
    while number != 0:
        r_m = number % 10
        if (r_m % 2) != 0:
            current_sum = current_sum + r_m
        number = number // 10
    return int(current_sum) 

def sum_even_digits(number):
    '''Choose the even numbers, then digit sum
    r_m: rightmost digit'''
    current_sum = 0
    while number != 0:
        r_m = number % 10
        if (r_m % 2) == 0:
            current_sum = current_sum + r_m
        number = number // 10
    return int(current_sum)

def sum_all_digits(number):
    '''Digit sum of all integer number
    r_m: rightmost digit'''
    current_sum = 0
    while number != 0:
        r_m = number % 10
        current_sum = current_sum + r_m
        number = number //10
    return int(current_sum) 

## REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
## OTHER THAN YOUR FUNCTION DEFINITION AND COMMENTS. You can (and should)
## use docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very beginning
## of the function suite. Everywhere else you should use comments.
