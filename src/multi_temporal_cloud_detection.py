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
    Row = row + sz
    Col = col + sz
    #Apply padding with nan add edge
    array = dic["blue"][date]
    array_with_margins = np.pad(array.astype(float),pad_width=sz,mode='constant',constant_values=np.nan)
    result = array_with_margins[Row - sz:Row + sz + 1, Col - sz:Col + sz + 1]

    return result

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



