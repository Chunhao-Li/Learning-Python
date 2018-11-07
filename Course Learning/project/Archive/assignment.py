"""COMP1730/6730 assignment S2 2018.

Coauthors: <u6489809>, <u6527752>, <u6486892>
Date: <20/10/2018>
"""
import csv
import math
import random
from visualise import show_vegetation_type
from visualise import show_vegetation_density
from visualise import show_wind_speed
from visualise import show_bushfire
from visualise import show_fire_risk


# The following functions must return the data in the form of a
# list of lists; the choice of data type to represent the value
# in each cell, for each file type, is up to you.

def load_vegetation_type(filename):
    """Load the vegetation_type file and returns a list of lists"""
    return load_csv(filename)


def load_vegetation_density(filename):
    """Load the vegetation_density file and returns a list of lists"""
    return load_csv(filename)


def load_wind_speed(filename):
    """Load the wind speed file and returns a list of lists"""
    return load_csv(filename)


def load_bushfire(filename):
    """Load the bushfire file and returns a list of lists"""
    return load_csv(filename)


def load_csv(filename):
    """This function can load the CSV files and return a list of lists.

    filename: string
    """
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        table = [row for row in reader]
        csvfile.close()
    return table


# The argument to this function is a wind speed map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_wind_speed
# function.

def highest_wind_speed(wind_speed_map):
    """Returns the highest wind speed as float.
    wind_speed_map: a list of lists
    """
    highest_lst = []
    for row in wind_speed_map:
        highest_lst.append(max(row))
    return float(max(highest_lst))


# The argument to this function is a vegetation type map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_vegetation_type
# function.


def count_cells(vegetation_type):
    """Print the number of cells of each kind of vegetation.
    vegetation_type: a list of lists
    Note : The result will only contain types appear in the table.
    """
    cells_dict = {}
    for row in vegetation_type:
        for element in row:
            if element != '':
                if element in cells_dict:
                    cells_dict[element] += 1
                else:
                    cells_dict[element] = 1
    for k in cells_dict:
        print(k, ':', cells_dict[k])


# The arguments to this function are a vegetation type map and
# a vegetation density map, both in the form of a list of lists.
# They are the same data structure that is returned by your
# implementations of the load_vegetation_type and load_vegetation_density
# functions, respectively.


def count_area(vegetation_type, vegetation_density):
    """Print the area of each kind of vegetation.
    vegetation_type: a list of lists
    vegetation_density: a list of lists
    Note : The result will only contain types appear in the table.
    """
    area_dict = {}
    cell_area = 100 * 100
    for i in range(len(vegetation_type)):
        j = 0
        for element in vegetation_type[i]:
            if element != '':
                if element in area_dict:
                    area_dict[element] += cell_area * \
                                          float(vegetation_density[i][j])
                else:
                    area_dict[element] = cell_area * \
                                         float(vegetation_density[i][j])
            j += 1
    for k in area_dict:
        print(k + ': ' + '{:.2f}'.format(area_dict[k]) + 'sq m')


# The arguments to this function are:
# x and y - integers, representing a position in the grid;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).

def fire_risk(x, y, vegetation_type, vegetation_density, wind_speed):
    """Calculate the fire risk for a cell.

    x,y: the index (col,row) of a cell.
    vegetation_type, vegetation_density, wind_speed: lists of lists."""
    factor = 0
    if wind_speed[y][x] == '' or math.floor(float(wind_speed[y][x])) == 0:
        return fire_risk_factor(x, y, vegetation_type, vegetation_density)

    else:
        nearby = math.floor(float(wind_speed[y][x]))
        row_upper = min([len(wind_speed), y + nearby + 1])  # upper bound of the row index range
        row_lower = max([0, y - nearby])
        col_upper = min([len(wind_speed[y]), x + nearby + 1])  # upper bound of the column index range
        col_lower = max([0, x - nearby])
        for y1 in range(row_lower, row_upper):
            for x1 in range(col_lower, col_upper):
                if abs(x1 - x) + abs(y1 - y) <= nearby:
                    factor += fire_risk_factor(x1, y1, vegetation_type, vegetation_density)
        return factor


def fire_risk_factor(x, y, vegetation_type, vegetation_density):
    """Return the fire risk factor for a single cell.

    x,y:the index of a cell.
    vegetation_type, vegetation_density: lists of lists.
    """
    if vegetation_type[y][x] == '':
        return 0
    elif vegetation_type[y][x] == 'Shrubland' or vegetation_type[y][x] == 'Pine Forest':
        a = 0.2
    elif vegetation_type[y][x] == 'Arboretum':
        a = 0.1
    elif vegetation_type[y][x] == 'Urban Vegetation' or vegetation_type[y][x] == 'Golf Course':
        a = 0.05
    else:
        a = 0
    return math.sqrt(a + float(vegetation_density[y][x]))


# The arguments to this function are an initial bushfire map (a list
# of lists, as returned by your implementation of the load_bushfire
# function), a vegetation type map (as returned by your implementation
# of the load_vegetation_type function), a vegetation density map (as
# returned by your implementation of load_vegetation_density) and a
# positive integer, representing the number of steps to simulate.

def simulate_bushfire(initial_bushfire, vegetation_type, vegetation_density, steps):
    """A simple simulation of the spread of a bushfire for a number of steps.
    This function returns a list of lists.

    initial_bushfire, vegetation_type, vegetation_density: lists of lists.
    steps: a positive integer.
    """
    new_bushfire = [row[:] for row in initial_bushfire]
    while steps > 0:
        fire_source = []  # a list contains the indices of fire cells
        for y in range(len(new_bushfire)):
            for x in range(len(new_bushfire[y])):
                if new_bushfire[y][x] == '1':
                    fire_source.append([y, x])

        for index in fire_source:
            y, x = index[0], index[1]
            row_upper = min([len(new_bushfire), y + 2])  # upper bound of the row index range
            row_lower = max([0, y - 1])
            col_upper = min([len(new_bushfire[y]), x + 2])  # upper bound of the column index range
            col_lower = max([0, x - 1])

            for i in range(row_lower, row_upper):
                for j in range(col_lower, col_upper):
                    if new_bushfire[i][j] == '0':
                        new_bushfire[i][j] = '1'
        steps -= 1
    return new_bushfire


# The arguments to this function are two bushfile maps (each a list
# of lists, i.e., same format as returned by your implementation of
# the load_bushfire function).

def compare_bushfires(bushfire_a, bushfire_b):
    """Return the percentage of cells that are the same of two bushfire maps.

    bushfire_a, bushfire_b: lists of lists.
    Note: bushfire_a and bushfire_b has the same number of cells.
    """
    same_cells = 0
    all_cells = 0  # the number of non-blank cells of either one table

    for i in range(len(bushfire_b)):
        for j in range(len(bushfire_b[i])):
            if bushfire_b[i][j] != '':
                all_cells += 1
                if bushfire_b[i][j] == bushfire_a[i][j]:
                    same_cells += 1
    return same_cells / all_cells


# The arguments to this function are:
# initial_bushfire - an initial bushfile map (a list of lists, same
#   as returned by your implementation of the load_bushfire function);
# steps - a positive integer, the number of steps to simulate;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).

def simulate_bushfire_stochastic(
        initial_bushfire, steps,
        vegetation_type, vegetation_density,
        wind_speed):
    """This function stochastically simulates fire spreading for a number
    of steps. It returns a list of lists.

    initial_bushfire, vegetation_type, vegetation_density, wind_speed: lists of lists
    steps: a positive integer
    """
    risk_factor = []  # A list contains fire risk factors of all cells
    for i in range(len(vegetation_type)):
        for j in range(len(vegetation_type[i])):
            risk_factor.append(fire_risk(j, i, vegetation_type,
                                         vegetation_density, wind_speed))
    min_factor = min(risk_factor)
    max_factor = max(risk_factor)
    new_bushfire = [row[:] for row in initial_bushfire]

    while steps > 0:
        fire_source = []  # A list contains indices of fire cells
        for y in range(len(new_bushfire)):
            for x in range(len(new_bushfire[y])):
                if new_bushfire[y][x] == '1':
                    fire_source.append([y, x])

        for index in fire_source:
            y, x = index[0], index[1]
            row_upper = min([len(new_bushfire), y + 2])  # upper bound of the row index range
            row_lower = max([0, y - 1])
            col_upper = min([len(new_bushfire[y]), x + 2])  # upper bound of the column index range
            col_lower = max([0, x - 1])

            for i in range(row_lower, row_upper):
                for j in range(col_lower, col_upper):
                    if new_bushfire[i][j] == '0':
                        random_factor = random.uniform(min_factor, max_factor)
                        risk = fire_risk(j, i, vegetation_type,
                                         vegetation_density, wind_speed)
                        if risk >= random_factor:
                            new_bushfire[i][j] = '1'
        steps -= 1
    return new_bushfire


if __name__ == '__main__':
    # If you want something to happen when you run this file,
    # put the code in this `if` block.
    pass
