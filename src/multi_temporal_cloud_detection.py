import datetime
from src.timeseries import extract_timeseries
import pandas as pd
import numpy as np


# Test 1 #
def mtcd_test1(dic, row, col):
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
def mtcd_test2(dic, row, col):
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

def test_3(dic, band, row, col):
    na_matrix = np.full((3, 3), np.nan)

    date = [key for key in dic[band].keys()][1]

    def index_error(index, row_im, col_im):
        try:
            np.put(na_matrix, [index], dic[band][date][row_im, col_im])
        except IndexError:
            na_matrix

    index_error(4, row, col)
    index_error(5, row, col + 1)
    index_error(7, row + 1, col)
    index_error(8, row + 1, col + 1)

    if row - 1 >= 0:
        index_error(0, row - 1, col - 1)
        index_error(1, row - 1, col)
        index_error(2, row - 1, col + 1)
    else:
        na_matrix

    if col - 1 >= 0:
        index_error(3, row, col - 1)
        index_error(6, row + 1, col - 1)
    else:
        na_matrix

def cor_test3(array1, array2):
    cov = np.mean((array1 - array1.mean()) * (array2 - array2.mean()))
    max_cov = array1.std() * array2.std()
    result = cov / max_cov
    if result > 0.5:
        return True
    else:
        return False


def mtcd(dic, band, row, col):
    # check the result of the 3 tests and returns
    # True when cloud, False when not cloud
    Test_1 = mtcd_test1(dic, row, col)
    Test_2 = mtcd_test2(dic, row, col)
    Test_3 = mtcd_test3(dic, band, row, col)
    if Test_1 == True and Test_2 == False and Test_3 == False:
        return True
    else:
        return False



