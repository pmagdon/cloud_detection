import datetime
from src.timeseries import extract_timeseries
import pandas as pd
import numpy as np
import math


# Test 1 #
def mtcd_test1(dic, row, col, date):
    # test if the temporal variation of reflectance on the blue band is big compared to a threshold
    # Big increase indicates cloud

    time_series_blue = extract_timeseries(dic, "blue", row, col)
    data_frame_blue = pd.DataFrame(time_series_blue)  # creates a data frame

    refl_blue_dayref = data_frame_blue["values"][0]  # extracts the pixel value of the reference image
    refl_blue_dayd = data_frame_blue["values"][1] # extracts the pixel value of an image

    dayd = datetime.datetime.strptime(data_frame_blue["dates"][0], "%Y-%m-%d")  # extracts the date value
    dayref = datetime.datetime.strptime(data_frame_blue["dates"][1], "%Y-%m-%d")  # extracts data value of reference image

    if refl_blue_dayd - refl_blue_dayref > 3 * (
        1 + (dayd - dayref).total_seconds() / (60 * 60 * 24) / 30):
        return True
    else:
        return False


# Test 2 #
def mtcd_test2(dic, row, col, date):
    # test if the variation of reflectance in the red band is much greater than in the blue band

    time_series_red = extract_timeseries(dic, "red", row, col)
    data_frame_red = pd.DataFrame(time_series_red)  # creates a data frame

    refl_red_dayref = data_frame_red["values"][0]  # extracts the pixel value of the reference image
    refl_red_dayd = data_frame_red["values"][1]  # extracts the pixel value of an image

    dayd = datetime.datetime.strptime(data_frame_red["dates"][0], "%Y-%m-%d")  # extracts the date value
    dayref = datetime.datetime.strptime(data_frame_red["dates"][1],
                                        "%Y-%m-%d")  # extracts data value of reference image

    if (refl_red_dayd - refl_red_dayref) > 150 * (dayd - dayref).total_seconds() / (60 * 60 * 24):
        return False
    else:
        return True


# Test 3 #

def test_3(dic, row, col, size, date):
    na_matrix = np.full((size, size), np.nan)

    date = [key for key in dic["blue"].keys()][1]

    half = math.floor(size/2)
    row_limit = dic["blue"][date].shape[0]
    col_limit = dic["blue"][date].shape[1]

    if row - half > 0 and row + half < row_limit and col - half > 0 and col + half < col_limit:
        np.put(na_matrix, [value for value in range(na_matrix.shape[0] ** 2)],
           dic["blue"][date][[row for row in range(row-half, row+half)],
                           [col for col in range(col-half, col+half)]])
    else: #

        return na_matrix

def cor_test3(array1, array2):
    cov = np.mean((array1 - array1.mean()) * (array2 - array2.mean()))
    max_cov = array1.std() * array2.std()
    result = cov / max_cov
    if result > 0.5:
        return True
    else:
        return False


def mtcd(dic, row, col, date):
    # check the result of the 3 tests and returns
    # True when cloud, False when not cloud
    Test_1 = mtcd_test1(dic, row, col, date)
    Test_2 = mtcd_test2(dic, row, col, date)
    Test_3 = cor_test3(dic, row, col, date)
    if Test_1 == True and Test_2 == False and Test_3 == False:
        return np.nan, date
    else:
        return True, date



