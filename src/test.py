import datetime
from src.timeseries import extract_timeseries
import pandas as pd
import numpy as np
import math


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


                ##################

na_matrix = np.full((3,3), np.nan)

size = 3
row, col = 526, 718  # for image

date_ref = [key for key in dictionary_blue_red["blue"].keys()][0]
date = [key for key in dictionary_blue_red["blue"].keys()][1]

np.put(na_matrix, [value for value in range(na_matrix.shape[0] ** 2)], [y for y in range(0, 9)])

###################


