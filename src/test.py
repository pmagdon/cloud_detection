import datetime
from src.timeseries import extract_timeseries
import pandas as pd
import numpy as np
import math


########## test 3 before craig´s code i############

def test_3(dic, row, col, size, date):

    na_matrix = np.full((size, size), np.nan)
    # Creates a matrix full of nan with the size "size"

    date = [key for key in dic["blue"].keys()][1]
    # The date of the image, used later for extracting the values from the dictionary
    half = math.floor(size/2)
    row_limit = dic["blue"][date].shape[0]
    col_limit = dic["blue"][date].shape[1]
    # Setup parameters: half and limits of the window

    if row - half > 0 and row + half < row_limit and col - half > 0 and col + half < col_limit:
        np.put(na_matrix, [value for value in range(na_matrix.shape[0] ** 2)],
           dic["blue"][date][[row for row in range(row-half, row+half)],
                           [col for col in range(col-half, col+half)]])
    else:
        row_window = row - math.floor(size / 2)
        col_window = col - math.floor(size / 2)
    # Setup the starting cell (of the window) This should always be the top left

        for i in range(0, row_window):
            row_window += 1
            for j in range(0, col_window):
                col_window += 1
            # For loop running over every cell in the window in order. Loop both updates the value of the cell in its
            # correct position while also updating the position counters for the next iteration of the loop
                if row - half > 0 and row + half < row_window and col - half > 0 and col + half < col_window:
                    np.put(na_matrix, [i, j], dic["blue"][date][row_window][col_window])

    return na_matrix


##########################
fun = {"blue": {"day1": np.arange(25).reshape(5,5)}}
print(fun["blue"]["day1"])


def test_3(dic, row, col, size, date):
    if size%2 == 0:
        raise ValueError(" Window size needs to be odd")

    na_matrix = np.full((size, size), np.nan)

    row_limit = dic["blue"][date].shape[0]
    col_limit = dic["blue"][date].shape[1]

    windowsize = int(size)
    halfwindow = math.floor(windowsize / 2)

    def get_values(array, row, col, halfwindow):
        array[row - halfwindow:row + halfwindow + 1, col - halfwindow:col + halfwindow + 1]

    if row - halfwindow >= 0 and row + halfwindow < row_limit and col - halfwindow >= 0 and col + halfwindow < col_limit:
        dic["blue"][date][row - halfwindow:row + halfwindow + 1, col - halfwindow:col + halfwindow + 1]

    else:
        for x in range(-halfwindow, (halfwindow + 1)):
            # Run for every column in the window in each row
            row_window = (row + x)
            for y in range(-halfwindow, (halfwindow + 1)):
                col_window = (col + y)
                if row_limit > row_window >= 0 and col_limit > col_window >= 0:
                    print(row_window, col_window, " is a usable cell")
    return na_matrix

image = np.arange(100).reshape(10,10)
#image = np.random.randint(0,100,100).reshape(10,10)

def moving_window(array, size,edge='nan'):
    """ Function to extract the values within an analysis window from an 2d Array
    Args:
        array:  the image from which to extract all the moving windows
        size: the siez of the movong window as odd number
        edge: a string argument to specify how to handle the edges
    Returns:
         None and prints all windows
    """

    if size%2 == 0:
        raise ValueError(" Size needs to be odd!")
    if edge != 'nan':
        raise ValueError(" Edge argument needs to of 'nan', ...")

    sz = math.floor(size / 2)
    #Apply padding with nan add edge
    array = np.pad(array.astype(float),pad_width=sz,mode='constant',constant_values=np.nan)

    for row in range(sz, array.shape[0]-sz):
        for col in range(sz, image.shape[1]-sz):
            print(array[row-sz:row + sz + 1, col-sz:col+sz+1])


moving_window(image, 3,edge='nan')

