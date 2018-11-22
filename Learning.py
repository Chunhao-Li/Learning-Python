# -*- coding: gbk -*-

import string
import datetime
import threading
import pickle
import time
import timeit
import re
import json
import math
import os
import random
import urllib.request
from collections import Counter
from collections import OrderedDict
from structshape import structshape


def print_params(*params):
    print(params)


def print_params2(title, *params):
    print(title)
    print(params)


def print_params_3(**params):
    print(params)


def print_params_4(y, x, *pospar, z=3, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)


def add(x, y):
    return x + y


# int_str = input("first:")
# first_int = int(int_str)
# int_str=input("second:")
# second_int = int(int_str)
# tens_count = 0
# loop_count = 0

# while first_int > 10 and second_int < 20:
#   if first_int == 10 or second_int == 10:
#      tens_count += 1
# first_int -= 5
# second_int += 5
# loop_count += 1

def story(**kwds):
    return 'Once upon a time, there was a ' \
           '%(job)s called %(name)s.' % kwds


def power(x, y, *others):
    if others:
        print('Recieved redundant parameters:', others)
    return pow(x, y)


def combine(parameter):
    print(parameter + globals()['parameter'])


# def change_global():
#     # global x
#     x = 1


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
        n_ls.append(sum(ls[:index + 1]))
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


def middle_func(ls):
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


def is_anagram(s1, s2):
    ls1 = sorted(list(s1))
    ls2 = sorted(list(s2))
    if ls1 == ls2:
        return True
    else:
        return False


def has_duplicates(ls):
    for e in ls:
        if ls.count(e) > 1:
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
        if s[i] == s[i + 1]:
            return True
    return False


def birth_pan():
    ls = []
    for i in range(23):
        m = random.randint(1, 12)
        if m in [1, 3, 5, 7, 8, 10, 12]:
            d = random.randint(1, 31)
        elif m in [4, 6, 9, 11]:
            d = random.randint(1, 30)
        else:
            d = random.randint(1, 29)
        ls += [(m, d)]
    return ls


def random_birth_days(n):
    """Returns a list of integers between 1 and 365, with length n.

    n: int

    returns: list of int
    """
    t = []
    for i in range(n):
        b_day = random.randint(1, 365)
        t.append(b_day)
    return t


def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.

    num_students: how many students in the group
    num_samples: how many groups to simulate

    returns: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_birth_days(num_students)
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
    # print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


# if __name__ == '__main__':
#   main1()np.array([0])


def make_word_list1():
    """Read lines from a file and builds a list using append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def factorial(n):
    result = n

    for i in range(1, n):
        result *= i
    return result


def power1(a, b):
    if a == 0:
        return 1
    else:
        return a * power(a, b - 1)


def search(seq, num, l=0, u=None):
    if u is None:
        u = len(seq) - 1
    if l == u:
        assert num == seq[u], "cannot find"
        return u
    else:
        middle = (l + u) // 2
        if num > seq[middle]:
            return search(seq, num, middle + 1, u)
        else:
            return search(seq, num, l, middle)


class Point:
    """Represents a pint in 2D space"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g,%g)' % (self.x, self.y)

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


def distance_between_points(a, b):
    return math.sqrt((a.x ** 2 - b.x ** 2) + (b.y * 8 ** 2 - a.y ** 2))


class Rectangle:
    """Represents a rectangle
    attributes: width, height, corner.
    """


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
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
    if math.sqrt((c.center.x - p.x) ** 2 + (c.center.y - p.y) ** 2) > c.radius:
        return False
    else:
        return True


def rect_in_circle(c, rect):
    import math
    rect_c = find_center(rect)
    d_line = math.sqrt((rect_c.x - rect.corner.x) ** 2 + (rect_c.y - rect.corner.y) ** 2)
    return d_line <= c.radius


def rect_circle_overlap():
    pass


class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

    def print_time(self):
        print("%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return t1 < t2


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
    sum_num = Time()
    sum_num.hour = t1.hour + t2.hour
    sum_num.minute = t1.minute + t2.minute
    sum_num.second = t1.second + t2.second

    if sum_num.second >= 60:
        sum_num.second -= 60
        sum_num.minute += 1

    if sum_num.minute >= 60:
        sum_num.minute -= 60
        sum_num.hour += 1
    return sum_num


def increment(time, seconds):
    time.second += seconds

    time.second += seconds % 60
    time.minute += seconds // 60
    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute = seconds % 60
        time.hour += seconds // 60


def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def f1(t):
    y = list(t)
    y.reverse()
    for i in range(len(y)):
        y[i] = chr(ord(y[i]) + 1)
    return ''.join(y)


def reverse_f1(y):
    ls = list(y)
    for i in range(len(ls)):
        ls[i] = chr(ord(ls[i]) - 1)
    ls.reverse()
    return ''.join(ls)


def sed(p_str, replace_str, source, dest):
    file1 = open(source)
    file2 = open(dest, 'w')
    for line in file1:
        line = line.replace(p_str, replace_str)
        file2.write(line)
    file1.close()
    file2.close()


# def main2():
#    p = 'pattern'
#    r = 'replace'
#    source = 'sed_tester.txt'
#    dest = source + '.replaced'
#    sed(p, r, source, dest)
#    
# if __name__ == '__main__':
#    main2()

# print("Who do you think I am")
# input()
# print("Oh, yes!")


# num = randint(1,100)
# print("Guess what I am thinking?")
# bingo = False
# while bingo == False:
#    a = eval(input())
#    if a < num:
#        print("TOO SMALL!")
#    if a > num:
#        print("TOO LARGE")
#    if a == num:
#        print("bingo")
#        bingo == True

# acc = 0
# for i in range(101):
#    acc += i
# print(acc)


def histogram(seq):
    count = dict()
    for elem in seq:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1
    return count


def invert_dictionary_sets(d):
    inverse_d = {}
    for k in d:
        if d[k] not in inverse_d:
            inverse_d[d[k]] = {k}# -*- coding: gbk -*-

import datetime
import threading
import pickle
import time
import timeit
import re
import json
import math
import os
import random
import urllib.request

from structshape import structshape


def print_params(*params):
    print(params)


def print_params2(title, *params):
    print(title)
    print(params)


def print_params_3(**params):
    print(params)


def print_params_4(y, x, *pospar, z=3, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)


def add(x, y):
    return x + y


# int_str = input("first:")
# first_int = int(int_str)
# int_str=input("second:")
# second_int = int(int_str)
# tens_count = 0
# loop_count = 0

# while first_int > 10 and second_int < 20:
#   if first_int == 10 or second_int == 10:
#      tens_count += 1
# first_int -= 5
# second_int += 5
# loop_count += 1

def story(**kwds):
    return 'Once upon a time, there was a ' \
           '%(job)s called %(name)s.' % kwds


def power(x, y, *others):
    if others:
        print('Recieved redundant parameters:', others)
    return pow(x, y)


def combine(parameter):
    print(parameter + globals()['parameter'])


# def change_global():
#     # global x
#     x = 1


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
        n_ls.append(sum(ls[:index + 1]))
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


def middle_func(ls):
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


def is_anagram(s1, s2):
    ls1 = sorted(list(s1))
    ls2 = sorted(list(s2))
    if ls1 == ls2:
        return True
    else:
        return False


def has_duplicates(ls):
    for e in ls:
        if ls.count(e) > 1:
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
        if s[i] == s[i + 1]:
            return True
    return False


def birth_pan():
    ls = []
    for i in range(23):
        m = random.randint(1, 12)
        if m in [1, 3, 5, 7, 8, 10, 12]:
            d = random.randint(1, 31)
        elif m in [4, 6, 9, 11]:
            d = random.randint(1, 30)
        else:
            d = random.randint(1, 29)
        ls += [(m, d)]
    return ls


def random_birth_days(n):
    """Returns a list of integers between 1 and 365, with length n.

    n: int

    returns: list of int
    """
    t = []
    for i in range(n):
        b_day = random.randint(1, 365)
        t.append(b_day)
    return t


def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.

    num_students: how many students in the group
    num_samples: how many groups to simulate

    returns: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_birth_days(num_students)
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
    # print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


# if __name__ == '__main__':
#   main1()np.array([0])


def make_word_list1():
    """Read lines from a file and builds a list using append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def factorial(n):
    result = n

    for i in range(1, n):
        result *= i
    return result


def power1(a, b):
    if a == 0:
        return 1
    else:
        return a * power(a, b - 1)


def search(seq, num, l=0, u=None):
    if u is None:
        u = len(seq) - 1
    if l == u:
        assert num == seq[u], "cannot find"
        return u
    else:
        middle = (l + u) // 2
        if num > seq[middle]:
            return search(seq, num, middle + 1, u)
        else:
            return search(seq, num, l, middle)


class Point:
    """Represents a pint in 2D space"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g,%g)' % (self.x, self.y)

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


def distance_between_points(a, b):
    return math.sqrt((a.x ** 2 - b.x ** 2) + (b.y * 8 ** 2 - a.y ** 2))


class Rectangle:
    """Represents a rectangle
    attributes: width, height, corner.
    """


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
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
    if math.sqrt((c.center.x - p.x) ** 2 + (c.center.y - p.y) ** 2) > c.radius:
        return False
    else:
        return True


def rect_in_circle(c, rect):
    import math
    rect_c = find_center(rect)
    d_line = math.sqrt((rect_c.x - rect.corner.x) ** 2 + (rect_c.y - rect.corner.y) ** 2)
    return d_line <= c.radius


def rect_circle_overlap():
    pass


class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

    def print_time(self):
        print("%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __lt__(self, other):
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return t1 < t2


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
    sum_num = Time()
    sum_num.hour = t1.hour + t2.hour
    sum_num.minute = t1.minute + t2.minute
    sum_num.second = t1.second + t2.second

    if sum_num.second >= 60:
        sum_num.second -= 60
        sum_num.minute += 1

    if sum_num.minute >= 60:
        sum_num.minute -= 60
        sum_num.hour += 1
    return sum_num


def increment(time, seconds):
    time.second += seconds

    time.second += seconds % 60
    time.minute += seconds // 60
    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute = seconds % 60
        time.hour += seconds // 60


def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def f1(t):
    y = list(t)
    y.reverse()
    for i in range(len(y)):
        y[i] = chr(ord(y[i]) + 1)
    return ''.join(y)


def reverse_f1(y):
    ls = list(y)
    for i in range(len(ls)):
        ls[i] = chr(ord(ls[i]) - 1)
    ls.reverse()
    return ''.join(ls)


def sed(p_str, replace_str, source, dest):
    file1 = open(source)
    file2 = open(dest, 'w')
    for line in file1:
        line = line.replace(p_str, replace_str)
        file2.write(line)
    file1.close()
    file2.close()


# def main2():
#    p = 'pattern'
#    r = 'replace'
#    source = 'sed_tester.txt'
#    dest = source + '.replaced'
#    sed(p, r, source, dest)
#
# if __name__ == '__main__':
#    main2()

# print("Who do you think I am")
# input()
# print("Oh, yes!")


# num = randint(1,100)
# print("Guess what I am thinking?")
# bingo = False
# while bingo == False:
#    a = eval(input())
#    if a < num:
#        print("TOO SMALL!")
#    if a > num:
#        print("TOO LARGE")
#    if a == num:
#        print("bingo")
#        bingo == True

# acc = 0
# for i in range(101):
#    acc += i
# print(acc)


def histogram(seq):
    count = dict()
    for elem in seq:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1
    return count


def invert_dictionary_sets(d):
    inverse_d = {}
    for k in d:
        if d[k] not in inverse_d:
            inverse_d[d[k]] = {k}
        else:
            inverse_d[d[k]].add(k)
    return inverse_d


def invert_dict(d):
    """Inverts a dictionary, returning a map from val to a list of keys.

    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.

    d: dict

    Returns: dict
    """
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


def dict_len(wordlist):
    d = {}
    for word in wordlist:
        if len(word) not in d:
            d[len(word)] = [word]
        else:
            d[len(word)].append(word)
    return d


def remove_newline_ls(path):
    f = open(path)
    ls = [line.strip() for line in f]
    return ls


def three_consecutive(wordlist):
    """Find words have three consecutive double letters"""
    len_dict = dict_len(wordlist)

    new_ls = []
    for ki in range(6, max(len_dict.keys())):
        for word in len_dict[ki]:
            i = 0
            while i + 5 < len(word):
                if word[i] == word[i + 1] \
                        and word[i + 2] == word[i + 3] \
                        and word[i + 4] == word[i + 5] \
                        and word[i] != word[i + 2] != word[i + 4]:
                    new_ls.append(word)
                i += 1
    return new_ls


def is_triple_double(word):  # From textbook
    """Tests if a word contains three consecutive double letters.

    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1
    return False


def find_triple_double(path):  # From textbook
    """Reads a word list and prints words with triple double letters."""
    fin = open(path)
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


def print_all(*args):
    print(args)


def suma_ll(*args):
    return sum(args)


def make_word_list():
    from urllib.request import urlopen
    #  file_obj = urlopen("https://cs.anu.edu.au/courses/comp1730/labs/lab7/")
    file_obj = urlopen("http://www.gutenberg.org/ebooks/42671.txt.utf-8")
    # file_obj = urlopen("http://www.gutenberg.org/cache/epub/42671/pg42671.txt.utf-8")
    ls = []
    #    for line in file_obj:
    #        line = line.split()
    #        ls.extend(line)

    import string
    for byte_seq in file_obj:
        line = byte_seq.decode()
        if line.strip() != '':
            line = line.rstrip('\n\r')
            exclude = set(string.punctuation)
            line = ''.join(ch for ch in line if ch not in exclude)
            word_list = line.split()
            ls.extend(word_list)
        # process line of text
    file_obj.close()
    return ls


def permutation_dict(d):
    ls = []  # list of closed sets

    for k in d:
        check = k
        set1 = set()
        while d[k] in d:
            if d[k] == check:
                set1.add(k)
                ls.append(set1)
                break
            else:
                set1.add(k)
                k = d[k]
    no_duplicate_ls = []
    for element in ls:
        if element not in no_duplicate_ls:
            no_duplicate_ls.append(element)

    return no_duplicate_ls


def has_duplicates_dict(lst):
    d = {}
    for element in lst:
        d.setdefault(element, []).append(element)
        if len(d[element]) > 1:
            #           print(d)
            return True
    return False


def has_duplicates_concise1(t):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = {}
    for i in t:
        if i in d:
            return True
        d[i] = True
    return False


def has_duplicates_concise2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)


def game_penalty_kick():
    #    score_player = 0
    #    score_computer = 0
    score = [0, 0]
    direct_ls = ['left', 'centre', 'right']
    while score[0] == score[1]:
        for i in range(5):
            print('==== Round %d - You kick! ====' % (i + 1))
            print("Choose one side to shoot:"), print('left, centre, right')
            player = input("Choose one side to shoot:")
            direct = random.choice(direct_ls)
            print('Computer saved ' + direct)
            if player != direct:
                score[0] += 1
                #            score_computer -= 1
                print('Goal!')
            else:
                score[1] += 1
                #            score_player -= 1
                print('Served')

            i += 1
    print('Score: %d(player) - %d(computer)' % (score[0], score[1]))
    if score[0] > score[1]:
        print('You Win!')
    else:
        print('You Lose.')


# game_penalty_kick()

def calculate_average_score():
    """Calculate the average scores of a person"""
    f = open('scores.txt')
    lines = f.readlines()
    #    print(lines)
    f.close()

    results = []

    for line in lines:
        #        print(line)
        data = line.split()
        #        print(data)

        sum_num = 0
        for score in data[1:]:
            point = int(score)
            if point < 60:
                continue
            sum_num += int(score)
        result = '%s\t:%d\n' % (data[0], sum_num)
        #        print(result)

        results.append(result)
    #    print(results)
    output = open('result.txt', 'w')
    output.writelines(results)
    output.close()


def struct_shape(ds):
    """Returns a string that describes the shape of a data structure.

    ds: any Python object

    Returns: string
    """
    typename = type(ds).__name__

    # handle sequences
    sequence = (list, tuple, set, type(iter('')))
    if isinstance(ds, sequence):
        t = []
        for i, j in enumerate(ds):
            t.append(structshape(j))
        rep = '%s of %s' % (typename, list_rep(t))
        return rep

    # handle dictionaries
    elif isinstance(ds, dict):
        keys = set()
        vals = set()
        for k, v in ds.items():
            keys.add(structshape(k))
            vals.add(structshape(v))
        rep = '%s of %d %s->%s' % (typename, len(ds),
                                   set_rep(keys), set_rep(vals))
        return rep

    # handle other types
    else:
        if hasattr(ds, '__class__'):
            return ds.__class__.__name__
        else:
            return typename


def list_rep(t):
    """Returns a string representation of a list of type strings.

    t: list of strings

    Returns: string
    """
    current = t[0]
    count = 0
    res = []
    for i in t:
        if i == current:
            count += 1
        else:
            append(res, current, count)
            current = i
            count = 1
    append(res, current, count)
    return set_rep(res)


def set_rep(s):
    """Returns a string representation of a set of type strings.

    s: set of strings

    Returns: string
    """
    rep = ', '.join(s)
    if len(s) == 1:
        return rep
    else:
        return '(' + rep + ')'


def append(res, typestr, count):
    """Adds a new element to a list of type strings.

    Modifies res.

    res: list of type strings
    typestr: the new type string
    count: how many of the new type there are

    Returns: None
    """
    if count == 1:
        rep = typestr
    else:
        rep = '%d %s' % (count, typestr)
    res.append(rep)


def most_frequent(string):
    """Takes a string and prints the letters in decreasing order of frequency"""
    d = {}
    freq_ls = []
    for char in string:
        #        if char not in d:
        #            d[char] = 1
        #        else:
        #            d[char] +=1
        d[char] = d.get(char, 0) + 1
    for i, freq in d.items():
        freq_ls.append((freq, i))
    freq_ls.sort(reverse=True)
    for freq, i in freq_ls:
        print(i)


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        #        # check the suits
        #        if self.suit < other.suit : return True
        #        if self.suit > other.suit : return False
        #
        #        # suits are the same... check ranks
        #        return self.rank < other.rank

        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def sort(self):
        self.cards.sort()

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        super().__init__()
        self.cards = []
        self.label = label


def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty


def find_weather():
    import city

    cityname = input('Which city do you want to search for?\n')
    citycode = city.get(cityname)
    if citycode:
        try:
            url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
            content = urllib.request.urlopen(url).read().decode()
            data = json.loads(content)
            result = data['weatherinfo']
            str_temp = '%s\n%s ~ %s' % (result['weather'],
                                        result['temp1'],
                                        result['temp2'])
            print(str_temp)
        except:
            print('Searching failed')

    else:
        print("Haven't find the city")


def find_city_code():
    url1 = 'http://m.weather.com.cn/data3/city.xml'
    content1 = urllib.request.urlopen(url1).read().decode()
    provinces = content1.split(',')

    result = 'city = {\n'
    url = 'http://m.weather.com.cn/data3/city%s.xml'
    for p in provinces:
        p_code = p.split('|')[0]
        if p_code == '23':
            url2 = url % p_code
            content2 = urllib.request.urlopen(url2).read().decode()
            cities = content2.split(',')

            # districts = []
            for c in cities:
                #    if c.split('|')[1] == '龙岩':

                c_code = c.split('|')[0]
                #        if c_code ==
                url3 = url % c_code
                content3 = urllib.request.urlopen(url3).read().decode()
                districts = content3.split(',')

                for d in districts:
                    d_pair = d.split('|')
                    d_code = d_pair[0]
                    name = d_pair[1]
                    url4 = url % d_code
                    content4 = urllib.request.urlopen(url4).read().decode()
                    code = content4.split('|')[1]
                    line = "  '%s':'%s',\n" % (name, code)
                    result += line
                    print(name + ':' + code)
    result += '}'
    f = open('city_code.py', 'w')
    f.write(result)
    f.close()


class MyClass:
    name = 'Sam'

    def say_hi(self):
        print('Hello %s' % self.name)


class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print('need %f hour(s)' % (distance / self.speed))


class Bike(Vehicle):
    pass


class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print('need %f fuels' % (distance * self.fuel))


if __name__ == '__main__':
    #    b = Bike(15.0)
    #    c = Car(80.0, 0.012)
    #    b.drive(100.0)
    #    c.drive(100.0)
    pass


def get_pos(n):
    return n / 2, n * 2


def func_determinant(a,b,c):
    discRoot = math.sqrt((b * b) - 4 * a * c)  # first pass
    root1 = (-b + discRoot) / (2 * a)  # solving positive
    root2 = (-b - discRoot) / (2 * a)  # solving negative
    return root1, root2
    # return (-b+(math.sqrt(b*b - 4*a*c)))/2*a, (-b-(math.sqrt(b*b - 4*a*c)))/2*a

def print_no_e():
    fin = open('words.txt')
    all_words = 0
    no_e_words = 0
    for line in fin:
        word = line.strip()
        all_words += 1
        if has_no_e(word):
            print(word)
            no_e_words += 1
    print(no_e_words / all_words)
    fin.close()

def has_no_e(word):
    for char in word:
        if char == 'e':
            return False
    return True

def avoids(word, string):
    for char in word:
        if char in string:
            return False
    return True

def num_of_no_forbidden():
    forbidden = input('Please input forbidden letters')
    count = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden):
            count += 1
    fin.close()
    return count

def find_combinations():
    adict = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        for char in word:
            char_set = set(char)
            for element in char_set:
                if element not in adict:
                    adict[element] = 1
                else:
                    adict[element] += 1
    frequency_list =[]
    for k in adict:
        frequency_list.append((adict[k], k))
    frequency_list.sort()
    combinations = []
    for (n, l) in frequency_list[:5]:
        combinations.append(l)
    fin.close()
    return str(combinations)

def uses_only(word, letters):
    word_lower = word.lower()
    for c in word_lower:
       if c != ' ':
        if c not in letters:
            return False
    return True

def uses_all1(word, letters):
    l_dict = {}
    for c in word:
        if c not in l_dict:
            l_dict[c] = 1
        else:
            l_dict[c] +=1
    keys= l_dict.keys()
    for char in letters:
        if char not in keys:
            return False
    return True

def uses_all2(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


def count_uses_all():
    letters = input('Please input some letters: ')
    fin = open('words.txt')
    count = 0
    for line in fin:
        word =line.strip()
        if uses_all(word, letters):
            count += 1
    fin.close()
    return count

def count_with_letters(func):
    letters = input('Please input some letters')
    count = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if func(word, letters):
            count += 1
    fin.close()
    return count


def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True

def count_aphabetical():
    count = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            count += 1
    fin.close()
    return count

def is_palindrome(word):
    i = 0
    j = len(word) - 1

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1

    return True

def get_30_movies():
    time_start = time.time()
    data = []
    for i in range(30):
        print('request movie: ', i)
        id = 1764796 + i
        url =  'https://api.douban.com/v2/movie/subject/%d' % id
        d = urllib.request.urlopen(url).read().decode()
        data.append(d)
        print(i, time.time()-time_start)
    print('data: ', len(data))

# b_list = [1,2,3,4]
# for i in b_list:
#     print(i)
#     print(i)

def find_all_files(path):
    lst = os.listdir(path)
    for e in lst:
        if os.path.isdir(e):
            new_path = os.path.join(path,e)
            lst.remove(e)
            lst.extend(find_all_files(new_path))
    return lst

def find_txt(lst):
    txt = re.findall(r'.\S*\.txt',' '.join(lst))
    return txt

def take_second(t):
    # new_lst = []
    return t[1]
    #     else:
    #         inverse_d[d[k]].add(k)
    # return inverse_d


def invert_dict(d):
    """Inverts a dictionary, returning a map from val to a list of keys.

    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.

    d: dict

    Returns: dict
    """
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


def dict_len(wordlist):
    d = {}
    for word in wordlist:
        if len(word) not in d:
            d[len(word)] = [word]
        else:
            d[len(word)].append(word)
    return d


def remove_newline_ls(path):
    f = open(path)
    ls = [line.strip() for line in f]
    return ls


def three_consecutive(wordlist):
    """Find words have three consecutive double letters"""
    len_dict = dict_len(wordlist)

    new_ls = []
    for ki in range(6, max(len_dict.keys())):
        for word in len_dict[ki]:
            i = 0
            while i + 5 < len(word):
                if word[i] == word[i + 1] \
                        and word[i + 2] == word[i + 3] \
                        and word[i + 4] == word[i + 5] \
                        and word[i] != word[i + 2] != word[i + 4]:
                    new_ls.append(word)
                i += 1
    return new_ls


def is_triple_double(word):  # From textbook
    """Tests if a word contains three consecutive double letters.
    
    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1
    return False


def find_triple_double(path):  # From textbook
    """Reads a word list and prints words with triple double letters."""
    fin = open(path)
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


def print_all(*args):
    print(args)


def suma_ll(*args):
    return sum(args)


def make_word_list():
    from urllib.request import urlopen
    #  file_obj = urlopen("https://cs.anu.edu.au/courses/comp1730/labs/lab7/")
    file_obj = urlopen("http://www.gutenberg.org/ebooks/42671.txt.utf-8")
    # file_obj = urlopen("http://www.gutenberg.org/cache/epub/42671/pg42671.txt.utf-8")
    ls = []
    #    for line in file_obj:
    #        line = line.split()
    #        ls.extend(line)

    import string
    for byte_seq in file_obj:
        line = byte_seq.decode()
        if line.strip() != '':
            line = line.rstrip('\n\r')
            exclude = set(string.punctuation)
            line = ''.join(ch for ch in line if ch not in exclude)
            word_list = line.split()
            ls.extend(word_list)
        # process line of text
    file_obj.close()
    return ls


def permutation_dict(d):
    ls = []  # list of closed sets

    for k in d:
        check = k
        set1 = set()
        while d[k] in d:
            if d[k] == check:
                set1.add(k)
                ls.append(set1)
                break
            else:
                set1.add(k)
                k = d[k]
    no_duplicate_ls = []
    for element in ls:
        if element not in no_duplicate_ls:
            no_duplicate_ls.append(element)

    return no_duplicate_ls


def has_duplicates_dict(lst):
    d = {}
    for element in lst:
        d.setdefault(element, []).append(element)
        if len(d[element]) > 1:
            #           print(d)
            return True
    return False


def has_duplicates_concise1(t):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = {}
    for i in t:
        if i in d:
            return True
        d[i] = True
    return False


def has_duplicates_concise2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)


def game_penalty_kick():
    #    score_player = 0
    #    score_computer = 0
    score = [0, 0]
    direct_ls = ['left', 'centre', 'right']
    while score[0] == score[1]:
        for i in range(5):
            print('==== Round %d - You kick! ====' % (i + 1))
            print("Choose one side to shoot:"), print('left, centre, right')
            player = input("Choose one side to shoot:")
            direct = random.choice(direct_ls)
            print('Computer saved ' + direct)
            if player != direct:
                score[0] += 1
                #            score_computer -= 1
                print('Goal!')
            else:
                score[1] += 1
                #            score_player -= 1
                print('Served')

            i += 1
    print('Score: %d(player) - %d(computer)' % (score[0], score[1]))
    if score[0] > score[1]:
        print('You Win!')
    else:
        print('You Lose.')


# game_penalty_kick()

def calculate_average_score():
    """Calculate the average scores of a person"""
    f = open('scores.txt')
    lines = f.readlines()
    #    print(lines)
    f.close()

    results = []

    for line in lines:
        #        print(line)
        data = line.split()
        #        print(data)

        sum_num = 0
        for score in data[1:]:
            point = int(score)
            if point < 60:
                continue
            sum_num += int(score)
        result = '%s\t:%d\n' % (data[0], sum_num)
        #        print(result)

        results.append(result)
    #    print(results)
    output = open('result.txt', 'w')
    output.writelines(results)
    output.close()


def struct_shape(ds):
    """Returns a string that describes the shape of a data structure.

    ds: any Python object

    Returns: string
    """
    typename = type(ds).__name__

    # handle sequences
    sequence = (list, tuple, set, type(iter('')))
    if isinstance(ds, sequence):
        t = []
        for i, j in enumerate(ds):
            t.append(structshape(j))
        rep = '%s of %s' % (typename, list_rep(t))
        return rep

    # handle dictionaries
    elif isinstance(ds, dict):
        keys = set()
        vals = set()
        for k, v in ds.items():
            keys.add(structshape(k))
            vals.add(structshape(v))
        rep = '%s of %d %s->%s' % (typename, len(ds),
                                   set_rep(keys), set_rep(vals))
        return rep

    # handle other types
    else:
        if hasattr(ds, '__class__'):
            return ds.__class__.__name__
        else:
            return typename


def list_rep(t):
    """Returns a string representation of a list of type strings.

    t: list of strings

    Returns: string
    """
    current = t[0]
    count = 0
    res = []
    for i in t:
        if i == current:
            count += 1
        else:
            append(res, current, count)
            current = i
            count = 1
    append(res, current, count)
    return set_rep(res)


def set_rep(s):
    """Returns a string representation of a set of type strings.

    s: set of strings

    Returns: string
    """
    rep = ', '.join(s)
    if len(s) == 1:
        return rep
    else:
        return '(' + rep + ')'


def append(res, typestr, count):
    """Adds a new element to a list of type strings.

    Modifies res.

    res: list of type strings
    typestr: the new type string
    count: how many of the new type there are

    Returns: None
    """
    if count == 1:
        rep = typestr
    else:
        rep = '%d %s' % (count, typestr)
    res.append(rep)


def most_frequent(string):
    """Takes a string and prints the letters in decreasing order of frequency"""
    d = {}
    freq_ls = []
    for char in string:
        #        if char not in d:
        #            d[char] = 1
        #        else:
        #            d[char] +=1
        d[char] = d.get(char, 0) + 1
    for i, freq in d.items():
        freq_ls.append((freq, i))
    freq_ls.sort(reverse=True)
    for freq, i in freq_ls:
        print(i)


class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        #        # check the suits
        #        if self.suit < other.suit : return True
        #        if self.suit > other.suit : return False
        #
        #        # suits are the same... check ranks
        #        return self.rank < other.rank

        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def sort(self):
        self.cards.sort()

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        super().__init__()
        self.cards = []
        self.label = label


def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty


def find_weather():
    import city

    cityname = input('Which city do you want to search for?\n')
    citycode = city.get(cityname)
    if citycode:
        try:
            url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
            content = urllib.request.urlopen(url).read().decode()
            data = json.loads(content)
            result = data['weatherinfo']
            str_temp = '%s\n%s ~ %s' % (result['weather'],
                                        result['temp1'],
                                        result['temp2'])
            print(str_temp)
        except:
            print('Searching failed')

    else:
        print("Haven't find the city")


def find_city_code():
    url1 = 'http://m.weather.com.cn/data3/city.xml'
    content1 = urllib.request.urlopen(url1).read().decode()
    provinces = content1.split(',')

    result = 'city = {\n'
    url = 'http://m.weather.com.cn/data3/city%s.xml'
    for p in provinces:
        p_code = p.split('|')[0]
        if p_code == '23':
            url2 = url % p_code
            content2 = urllib.request.urlopen(url2).read().decode()
            cities = content2.split(',')

            # districts = []
            for c in cities:
                #    if c.split('|')[1] == '龙岩':

                c_code = c.split('|')[0]
                #        if c_code ==
                url3 = url % c_code
                content3 = urllib.request.urlopen(url3).read().decode()
                districts = content3.split(',')

                for d in districts:
                    d_pair = d.split('|')
                    d_code = d_pair[0]
                    name = d_pair[1]
                    url4 = url % d_code
                    content4 = urllib.request.urlopen(url4).read().decode()
                    code = content4.split('|')[1]
                    line = "  '%s':'%s',\n" % (name, code)
                    result += line
                    print(name + ':' + code)
    result += '}'
    f = open('city_code.py', 'w')
    f.write(result)
    f.close()


class MyClass:
    name = 'Sam'

    def say_hi(self):
        print('Hello %s' % self.name)


class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print('need %f hour(s)' % (distance / self.speed))


class Bike(Vehicle):
    pass


class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print('need %f fuels' % (distance * self.fuel))


if __name__ == '__main__':
    #    b = Bike(15.0)
    #    c = Car(80.0, 0.012)
    #    b.drive(100.0)
    #    c.drive(100.0)
    pass


def get_pos(n):
    return n / 2, n * 2


def func_determinant(a,b,c):
    discRoot = math.sqrt((b * b) - 4 * a * c)  # first pass
    root1 = (-b + discRoot) / (2 * a)  # solving positive
    root2 = (-b - discRoot) / (2 * a)  # solving negative
    return root1, root2
    # return (-b+(math.sqrt(b*b - 4*a*c)))/2*a, (-b-(math.sqrt(b*b - 4*a*c)))/2*a

def print_no_e():
    fin = open('words.txt')
    all_words = 0
    no_e_words = 0
    for line in fin:
        word = line.strip()
        all_words += 1
        if has_no_e(word):
            print(word)
            no_e_words += 1
    print(no_e_words / all_words)
    fin.close()

def has_no_e(word):
    for char in word:
        if char == 'e':
            return False
    return True

def avoids(word, string):
    for char in word:
        if char in string:
            return False
    return True

def num_of_no_forbidden():
    forbidden = input('Please input forbidden letters')
    count = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden):
            count += 1
    fin.close()
    return count

def find_combinations():
    adict = {}
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        for char in word:
            char_set = set(char)
            for element in char_set:
                if element not in adict:
                    adict[element] = 1
                else:
                    adict[element] += 1
    frequency_list =[]
    for k in adict:
        frequency_list.append((adict[k], k))
    frequency_list.sort()
    combinations = []
    for (n, l) in frequency_list[:5]:
        combinations.append(l)
    fin.close()
    return str(combinations)

def uses_only(word, letters):
    word_lower = word.lower()
    for c in word_lower:
       if c != ' ':
        if c not in letters:
            return False
    return True

def uses_all1(word, letters):
    l_dict = {}
    for c in word:
        if c not in l_dict:
            l_dict[c] = 1
        else:
            l_dict[c] +=1
    keys= l_dict.keys()
    for char in letters:
        if char not in keys:
            return False
    return True

def uses_all2(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


def count_uses_all():
    letters = input('Please input some letters: ')
    fin = open('words.txt')
    count = 0
    for line in fin:
        word =line.strip()
        if uses_all(word, letters):
            count += 1
    fin.close()
    return count

def count_with_letters(func):
    letters = input('Please input some letters')
    count = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if func(word, letters):
            count += 1
    fin.close()
    return count


def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True

def count_aphabetical():
    count = 0
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            count += 1
    fin.close()
    return count

def is_palindrome(word):
    i = 0
    j = len(word) - 1

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1

    return True

def get_30_movies():
    time_start = time.time()
    data = []
    for i in range(30):
        print('request movie: ', i)
        id = 1764796 + i
        url =  'https://api.douban.com/v2/movie/subject/%d' % id
        d = urllib.request.urlopen(url).read().decode()
        data.append(d)
        print(i, time.time()-time_start)
    print('data: ', len(data))

# b_list = [1,2,3,4]
# for i in b_list:
#     print(i)
#     print(i)

def find_all_files(path):
    lst = os.listdir(path)
    for e in lst:
        if os.path.isdir(e):
            new_path = os.path.join(path,e)
            lst.remove(e)
            lst.extend(find_all_files(new_path))
    return lst

def find_txt(lst):
    txt = re.findall(r'.\S*\.txt',' '.join(lst))
    return txt

def take_second(t):
    # new_lst = []
    return t[1]

def charge_up():

    in_index = input('''Choose an operation:
    1. charge up
    2. check balance
    3. detail of income and expenditure'''
                     )
    if in_index == '1':
        f = open('Tolly Book.txt', 'a')
        amount = input('Amount: ')
        item = input('Item: ')
        f.write(str(datetime.date.today()) + ' ' +amount + ' ' + item + '\n')
        f.close()
        print('Data has been recorded.')
        charge_up()

    if in_index == '2':
        acc = 0
        f = open('Tolly Book.txt', 'r')
        lines = f.readlines()
        for line in lines:
            amount = re.findall(r'-?\d+\s', line[10:])
            acc += float(amount[0])
        print(acc)
        f.close()
        charge_up()

    if in_index == '3':
        f = open('Tolly Book.txt', 'r')
        lines = f.readlines()
        for line in lines:
            line.strip()
            print(line,end='')
        f.close()
        charge_up()

# def do_something(path):
#     f = open(path)
#     lines = f.readlines()
#     for line in lines:
#         line.strip()
#         for w

def monty_hall_problem():
    times = input("Please input a number: ")
    switch_win = 0
    stay_win = 0
    switch = 0
    stay = 0
    acc = 1
    while acc <= int(times):
        a = "car"
        b = "goat1"
        c = "goat2"
        x = random.choice([a,b,c])
        if x == a:
            x = random.choice([1,2,3])
            if x == 1:
                stay += 1
                stay_win += 1
            if x == 2 or x == 3:
                switch += 1
        if x == b :
            x = random.choice([1,2,3])
            if x == 1:
                switch += 1
                switch_win += 1
            if x == 2:
                stay += 1
            if x == 3:
                switch += 1
        if x == c:
            x = random.choice([1,2,3])
            if x == 1:
                switch += 1
                switch_win += 1
            if x == 2:
                switch += 1
            if x == 3:
                stay += 1
        acc += 1
    all_win = switch_win + stay_win
    print('total: %d'%int(times))
    print('switch: %d'%switch)
    print('switch win: ' + str(switch_win) + '('+ str(100 *switch_win/switch) + '%)' )
    print('stay: %d'%stay)
    print('stay win: ' + str(stay_win) + '(' + str(100 * stay_win/ stay) + '%)')

def lottery():
    red_ball = list(range(1,34))
    blue_ball = list(range(1,17))
    red_selection = []
    for i in range(6):
        rb = random.choice(red_ball)
        red_ball.remove(rb)
        red_selection.append(rb)
    bb = random.choice(blue_ball)
    print("Red Ball: ", end='')
    for b in red_selection:
        if b < 10:
            print('0{:d} '.format(b),end='')
        else:
            print(str(b)+' ',end='')
    print(' ')
    print("Blue Ball: ", end='')
    if bb < 10:
        print('0{:d}'.format(bb))
    else:
        print(bb)


# def count_words(path):
    # file = open(path,'rb')
    # lines = file.readlines()
    # file.close()
    # words_list = []
    # sq = string.whitespace + string.ascii_letters + string.punctuation
    # for line in lines:
    #     line = str(line)
    #
    #     line.strip(sq)
    #     line = line.lower()
    #     words_list.extend(line.split())
    # word_counter = Counter(words_list)
    # s_count = word_counter.most_common(100)
    # for i in range(len(s_count)):
    #     # print(type(s_count[i][0]))
    #     print('{0:d}.{1[0]:3s}{1[1]:4d}'.format(i+1,s_count[i]))

    # with open(rpath,'r')

def NovelRe(Novel):
    content = open(Novel, 'r',encoding="latin-1").read().lower()
    words = []
    pattern = r"(?<!')\b[a-zA-Z]{2}[a-zA-Z]+\b"
    tmp = re.findall(pattern, content)
    DropList = ['you','your','he','him','his','she','her','they','them','their','where','when','what','who','which','there','said','had','don','mer','for','jul','its','his','with','charles','elecbook','classics','charlotte','bront','aesop','fables','dickens','tale','and','the','that','was']
    for word in DropList:
        tmp = [x for x in tmp if x!=word]
    for x in tmp:
        words.append(x)
    Count = Counter(words).most_common(100)
    return Count


def Output():
    NovelList = ['a tale of two cities.txt', "Aesop's Fables.txt", 'Jane Eyre.txt',
                 'Oliver Twist.txt', 'Romeo and Juliet.txt']
    for novel in NovelList:
        print(novel[:-4] + '\n' + '========================================')
        WordList = NovelRe(novel)
        i = 1

        # wordsum = 0
        # for word in WordList:
        #     wordsum += word[1]

        for word in WordList:
            # print(str(i) + '.' + '\t' + str(word[0]) + '\t' + str('%.5f%%' % (word[1] / wordsum)))
            # print(str(i) + '.' + '\t' + str(word[0]) + '\t' + str(word[1]))
            print("{0:<5s}{1:10s}{2:2d}".format(str(i)+'.',str(word[0]),word[1]))
            i += 1
        print('\n')
        break
#
# # def slice_in_place(a_list, start, end):
# #     length = len(a_list)
# #     for i in range(len(a_list)):
# #
# #         if i not in range(start%length,end%length):
# #             a_list.pop(i)
def funX(a_list):
    x = a_list.pop(0)
    i = 0
    while i < len(a_list):
        if a_list[i] == x:
            a_list.pop(i)
        else:
            i += 1


def largest_palindrome_prod(len_1, len_2):
    num1 = sorted(generate_integers(len_1), reverse=True)
    num2 = sorted(generate_integers(len_2), reverse=True)

    for i in num1:
        for j in num2:
            number = i * j
            if is_palindrome_number(number):
                return number


def generate_integers(len_digit):
    base = list(range(1, 10))
    len_digit -= 1
    digits = range(10)
    output = base
    while len_digit >= 1:
        base = list(map(lambda x: x * 10, output))
        output = []
        for i in base:
            for j in digits:
                output.append(i + j)
        len_digit -= 1
    return output


def is_palindrome_number(n):
    str_num = str(n)
    i = 0
    j = len(str_num) - 1

    while i < j:
        if str_num[i] != str_num[j]:
            return False
        i += 1
        j -= 1

    return True


def largest_palindrome_prod2(len_1, len_2):
    new_list = []

    for i in range(1, int('9' * len_1) + 1):
        for j in range(1, int('9' * len_2) + 1):
            a = list(str(i * j))
            a.reverse()
            if list(str(i * j)) == a:
                new_list.append(i * j)
    return max(new_list)

def invert_dict(A):
    invA = {}
    for key in A.keys():
        invA[A[key]] = key
    return invA

def ceasar_cipher_encode(string, n):
    new_list = []
    for elem in string:
        if ord(elem) > ord('z') or ord(elem) < ord('A'):
            new_list.append(elem)
            continue
        num = ord(elem) + n
        if elem.isupper():
            if num > ord('Z'):
                num -= 26
        if num > ord('z'):
            num -= 26
        new_list.append(chr(num))
    return ''.join(new_list)

def nested_sets(A , B):
    if A == []:
        return True
    inner_lstA = []
    inner_lstB = []
    for el in A:
        if type(el) != list:
            if el not in B:
                return False
        else:
            inner_lstA.append(el)
    if inner_lstA == []:
        return True

    for el in B:
        if type(el) == list:
            inner_lstB.append(el)

    output_bools = []
    for i in inner_lstA:
        for j in inner_lstB:
            output_bools.append(nested_sets(i, j))
    output = any(output_bools)
    return output

def index_of_repetion(seq):
    repetion = []
    i = 0
    while i < len(seq):
        repetion.append(seq[i])
        k = len(seq) / len(repetion)
        if int(k) == k:
            if int(k)*repetion == list(seq):
                return int(k)
        i += 1
    return 1

def remove_all(el, alist):
    while el in alist:
        i = alist.index(el)
        alist.pop(i)

def monkey_buy_bananas():
    day = 2
    price = 2 **(int(day/21))
    o_quantity = 10 // price
    n_quantity = day*10 // price
    while n_quantity > o_quantity:
        o_quantity = n_quantity
        day += 1
        price = 2 ** (int(day / 21))
        n_quantity = day*10 // price
    return day


