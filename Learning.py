def print_params(*params):
	print(params)
    
def print_params2(title,*params):
    print(title)
    print(params)
    
def print_params_3(**params):
    print(params)
    
def print_params_4(x,y,z=3,*pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)
    
def add(x,y):
    return x+y

#int_str = input("first:")
#first_int = int(int_str)
#int_str=input("second:")
#second_int = int(int_str)
#tens_count = 0
#loop_count = 0

#while first_int > 10 and second_int < 20:
 #   if first_int == 10 or second_int == 10: 
  #      tens_count += 1
   # first_int -= 5
    #second_int += 5 
   # loop_count += 1

def story(**kwds):
    return 'Once upon a time, there was a '\
        '%(job)s called %(name)s.' % kwds

def power(x,y, *others):
    if others:
        print('Recieved redundant parameters:', others)
    return pow(x,y)

def combine(parameter):
    print(parameter + globals()['parameter'])
    
def change_global():
    global x
    x=1
    
def recursion():
     return recursion()

def nested_sum(ls):
    acc = 0
    for i in ls:
        acc += sum(i)
    return acc

def cumsum(ls):
    n_ls = []
    index = 0
    while index < len(ls):
        n_ls.append(sum(ls[:index+1])) 
        index += 1
    return n_ls

def cumsum1(t):
    """Computes the cumulative sum of the numbers in t.

    t: list of numbers

    returns: list of numbers
    """
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res


def middle(ls):
    m_ls = ls[1:-1]
    return m_ls

def chop(ls):
    ls.pop()
    ls.pop(0)
    
def is_sorted(ls):
    if ls == sorted(ls):
        return True
    else:
        return False
    
def is_sorted1(t):
    """Checks whether a list is sorted.

    t: list

    returns: boolean
    """
    return t == sorted(t)
    
def is_anagram(s1,s2):
    ls1 = sorted(list(s1))
    ls2 = sorted(list(s2))
    if ls1 == ls2 :
        return True
    else:
        return False
    
def has_duplicates(ls):
    for e in ls:
        if ls.count(e) >1:
            return True
    return False

def has_duplicates1(t):
    """Returns True if any element appears more than once in a sequence.

    t: list

    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()

    # check for adjacent elements that are equal
    for i in range(len(s)):
        if s[i] == s[i+1]:
            return True
    return False


import random
def Birth_pan():
    ls = []
    matches = 0
    for i in range(23):
        m = random.randint(1,12)
        if m in [1,3,5,7,8,10,12]:
            d = random.randint(1,31)
        elif m in [4,6,9,11]:
            d = random.randint(1,30)
        else:
            d = random.randint(1,29)
        ls += [(m,d)]
    return ls

def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length n.

    n: int

    returns: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.

    num_students: how many students in the group
    num_samples: how many groups to simulate

    returns: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count


def main():
    """Runs the birthday simulation and prints the number of matches."""
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


    
def main1():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))
    
#if __name__ == '__main__':
 #   main1()np.array([0])

 
def make_word_list1():
    '''Read lines from a file and builds a list using append.'''
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def factorial(n):
    result = n

    for i in range(1,n):
        result *= i
    return result

def power1(a,b):
    if a == 0:
        return 1
    else:
        return a*power(a,b-1)
    
def search(seq,num,l=0,u=None):
    if u is None: u = len(seq)-1
    if l == u:
        assert num == seq[u], ("cannot find")
        return u
    else:
        middle = (l+u)//2
        if num > seq[middle]:
            return search(seq,num,middle+1,u)
        else:
            return search(seq,num,l,middle)
        
        
class Point:
    '''Represents a pint in 2D space'''
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(p):
        return '(%g,%g)' % (p.x,p.y)
    
    def add_point(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)
        
    def add_tuple(self, other):
        self.x += other[0]
        self.y += other[1]
        return self
    
    def __radd__(self, other):
        return self.__add__(other)
    
import math

def distance_between_points(a,b):
    return math.sqrt((a.x**2-b.x**2)+(b.y*8**2-a.y**2))

class Rectangle:
    """Represents a rectangle
    attributes: width, height, corner.
    """
    
def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight
    
def move_rectangle(rect, dx, dy):
    import copy
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx 
    new_rect.corner.y += dy
    return new_rect
    
class Circle:
    """represents a circle
    Attributes:..."""
    
def point_in_circle(c, p):
    import math
    if math.sqrt((c.center.x-p.x)**2 + (c.center.y-p.y)**2) > c.radius:
        return False
    else:
        return True
    
def rect_in_circle(c, rect):
    import math
    rect_c = find_center(rect)
    d_line = math.sqrt((rect_c.x-rect.corner.x)**2 + (rect_c.y-rect.corner.y)**2)
    return d_line <= c.radius
    
def rect_circle_overlap(c, rect):
    pass

class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """
    def print_time(self):
        print("%.2d:%.2d:%.2d" %(self.hour,self.minute,self.second))
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
    
    def add_time (self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
     
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
        
    def __radd__(self, other):
        return self.__add__(other)
    
def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time

def is_after(t1, t2):
    """Returns True if t1 is after t2; false otherwise."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)
    
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.second >= 60:
       sum.second -= 60
       sum.minute += 1
        
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour +=1
    return sum

def increment(time, seconds):
    time.second += seconds
    
    time.second += seconds % 60
    time.minute += seconds // 60
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    
    
    if time.minute >= 60:
        time.minute = seconds % 60
        time.hour +=  seconds // 60
        
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))
import os        
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
            
def f1(x):
    y = list(x)
    y.reverse()
    for i in range( len( y ) ):
        y[i] = chr(ord(y[i])+1)
    return ''.join( y )

def reversef1(y):
    ls = list(y)
    for i in range(len(ls)):
        ls[i] = chr(ord(ls[i])-1)
    ls.reverse()
    return ''.join(ls)
    
def sed(p_str,replace_str,source,dest):
    
        file1 = open(source, 'r')
        file2 = open(dest, 'w')
        for line in file1:
            line = line.replace(p_str, replace_str)
            file2.write(line)
        file1.close()
        file2.close()
  
        
#def main2():
#    p = 'pattern'
#    r = 'replace'
#    source = 'sed_tester.txt'
#    dest = source + '.replaced'
#    sed(p, r, source, dest)
#    
#if __name__ == '__main__':
#    main2()
        
#print("Who do you think I am")
#input()
#print("Oh, yes!")
        

#num = randint(1,100)
#print("Guess what I am thinking?")
#bingo = False
#while bingo == False:
#    a = eval(input())
#    if a < num:
#        print("TOO SMALL!")
#    if a > num:
#        print("TOO LARGE")
#    if a == num:
#        print("bingo")
#        bingo == True
        
acc = 0
for i in range(101):
    acc += i
print(acc)