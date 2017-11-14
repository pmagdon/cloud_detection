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

def moving_window(dic, date, row, col, size, edge='nan'):
    """ Function to extract the values within an analysis window from an 2d Array
    Args:
        dic: the dictionary where the image is stored
        date: the date of the image from which to extract the moving window and, at the same time, the key of the
              dictionary
        row, col = the pixel number of row and column of the image which will be the center of the moving window
        size: the size of the moving window as odd number
        edge: a string argument to specify how to handle the edges
    Returns:
         Prints the moving window
    """
    if size%2 == 0:
        raise ValueError(" Size needs to be odd!")
    if edge != 'nan':
        raise ValueError(" Edge argument needs to of 'nan', ...")

    sz = math.floor(size / 2) # the floor of the half of the window
    Row = row + sz # to adjust the indexing which will change depending on the size of the window
    Col = col + sz
    #Apply padding with nan add edge
    array = dic["blue"][date]
    array_with_margins = np.pad(array.astype(float),pad_width=sz, mode='constant',constant_values=np.nan)
    result = array_with_margins[Row - sz:Row + sz + 1, Col - sz:Col + sz + 1]

    return result

def cor_test3(array1, array2):
    cov = np.nanmean((array1 - np.nanmean(array1)) * (array2 - np.nanmean(array2)))
    max_cov = np.nanstd(array1) * np.nanstd(array2)
    result = abs(cov / max_cov)
    if result > 0.5:
        return True
    else:
        return False


def mtcd(dic, row, col, date, size):
    # check the result of the 3 tests and returns
    # True when cloud, False when not cloud
    date_ref =
    Test_1 = mtcd_test1(dic, row, col, date)
    Test_2 = mtcd_test2(dic, row, col, date)
    array1 = moving_window(dic, date, row, col, size, edge='nan')
    array2 = moving_window(dic, date_ref, row, col, size, edge='nan')
    Test_3 = cor_test3(array1, array2)
    if Test_1 == True and Test_2 == False and Test_3 == False:
        return np.nan
    else:
        return True



