# -*- coding: gbk -*-

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

