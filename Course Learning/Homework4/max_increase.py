## COMP1730/6730 S2 2018 - Homework 4
# Submission is due 9am, Monday the 17th of September, 2018.

## YOUR ANU ID: u6527752
## YOUR NAME: Chunhao Li

## Implement the function max_increase below.
## (The statement "pass" is just a placeholder that does nothing: you
## should replace it.)
## You can define other functions if it helps you decompose the problem
## and write a better organised and/or more readable solution.

def max_increase(seq):
    ''' seq is a sequence whose elements are numbers.
    This function returns the maximum increase 
    from one element in seq to an element at a higher index'''
    if len(seq) < 2:
        return 0
    else:
        ls = max_increase_ls(seq)
        return max(ls)
                
def max_increase_ls(seq):
    '''To make a list of increments'''
    index = 0
    increase_ls = []
    while index < len(seq)-1:
        l_num = seq[index]
        h_num = max(seq[index:])
        m_increase = h_num - l_num
        increase_ls += [m_increase]
        index += 1
    return increase_ls
                






## REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
## OTHER THAN YOUR FUNCTION DEFINITION AND COMMENTS.
