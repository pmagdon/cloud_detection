import datetime
import math
import numpy as np
from src.search_reference import search_reference, search_references_list


def mtcd_test1(date, row, col, dic_values, dic_mask, par1):
    """
    Test the temporal variation of reflectance on the blue band comparing it to a threshold which is a function of the
    time interval. A big increase (True) indicates cloud.

    To compare the values of the image with the most recent cloud free reference, first extract the reference values
    (date and pixel value) to a list with the search_reference function. Extract the current values of the blue band
    for the selected pixel defined by its row and its column (parameters) from the values dictionary using as key the
    given date parameter. Compare the variation between the current pixel value and the cloud free reference value with
    a threshold that is a function of the time interval between the two images. If the pixel value variation is bigger
    than the threshold, classify the pixel as cloud (True) and if not, as cloud free (False).

    :param str date: The date of the image which is analysed at the moment.
    :param int row: The row of the pixel.
    :param int col: The column of the pixel.
    :param object dic_values: The dictionary with the dates and the pixel values of the image as arrays.
    :param object dic_mask: The dictionary with the dates and the cloud mask for the images.
    :param int par1: The percentage of variation in the blue band.
    :return: True if cloudy pixel, False if cloud free pixel
    """

    reference = search_reference(dic_values, dic_mask, row, col, "blue")

    date_ref = datetime.datetime.strptime(reference[0], "%Y-%m-%d")
    value_ref = reference[1]

    current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    current_value = dic_values["blue"][date][row, col]

    current_value_mean = np.nanmean(dic_values["blue"][date])
    ref_value_mean = np.nanmean(dic_values["blue"][reference[0]])
    if current_value_mean / ref_value_mean > 1.5 or current_value_mean / ref_value_mean < 0.5:
        par1 *= 1.6

    if current_value == 0 and current_value_mean == 0:
        return -999
    elif current_value - value_ref > par1 * (
        1 + (current_date - date_ref).total_seconds() / (60 * 60 * 24) / 30):
        return True
    else:
        return False


# Test 2 #

def mtcd_test2(date, row, col, dic_values, dic_mask, par2):
    """
    Test the variation of reflectance in the red band in comparision with the variation in the blue band.

    A big variation in the red band in comparision with the variation in the blue band indicates that the variation in
    the blue band is possibly not due to a cloud.

    :param  str date: The date of the image which is analysed at the moment.
    :param int row: The row of the pixel.
    :param int col: The column of the pixel.
    :param object dic_values: The dictionary with the dates and the pixel values of the image as arrays.
    :param object dic_mask: The dictionary with the dates and the cloud mask for the images.
    :param int par2: The percentage of variation between the red and the blue band.
    :return: True if the variation of the blue band is bigger (cloud) and false if it is not (not cloud).
    """
    ref_blue = search_reference(dic_values, dic_mask, row, col, "blue")
    ref_red = search_reference(dic_values, dic_mask, row, col, "red")

    value_ref_red = ref_red[1]
    current_value_red = dic_values["red"][date][row, col]

    value_ref_blue = ref_blue[1]
    current_value_blue = dic_values["blue"][date][row, col]

    if (current_value_red - value_ref_red) > par2 * (current_value_blue - value_ref_blue):
        return False
    else:
        return True


def analysis_window(dic, date, row, col, size, edge='nan'):
    """
    Extract the values within an analysis window from an 2D-array.

    The window is a square which size is defined by the parameter size. Size needs to be odd, since a central value is
    necessary for the analysis. The parameters row and column (of the image) define the central value for the window.
    Identify the half of the window, where the central value is placed. Place an NAN edge around the image whose width
    depends on the size of the window. This will make possible to extract the values placed at the edge of the image
    without getting an error. The NAN edge will modify the indexing, therefore adjust the row and the column values
    depending on the size of half of the window. Extract from the image array with margins the values within the
    analysis window.

    :param object dic: The dictionary with the dates and the pixel values of the image as arrays.
    :param str date: The date of the image.
    :param int row: The row of the pixel.
    :param int col: The column of the pixel.
    :param int size: The size of the analysis window.
    :param str edge: The value of the edge of the image.
    :return: The window as array with the image values.
    """

    if size%2 == 0:
        raise ValueError(" Size needs to be odd!")
    if edge != 'nan':
        raise ValueError(" Edge argument needs to be 'nan'")

    half_window = math.floor(size / 2)

    row_adjusted = row + half_window
    col_adjusted = col + half_window

    array = dic["blue"][date]
    array_with_margins = np.pad(array.astype(float), pad_width=half_window, mode='constant', constant_values=np.nan)
    result = array_with_margins[row_adjusted - half_window:row_adjusted + half_window + 1,
                                col_adjusted - half_window:col_adjusted + half_window + 1]

    return result


def cor_test3(array1, array2, corr):
    """
    Calculate the correlation between two arrays and return True if this is above a given coefficient.

    :param object array1: The first array.
    :param object array2: The second array.
    :param int corr: The correlation coefficient above which True is returned.
    :return: True if the correlation is above the given correlation coefficient and False if not.
    """
    cov = np.nanmean((array1 - np.nanmean(array1)) * (array2 - np.nanmean(array2)))
    max_cov = np.nanstd(array1) * np.nanstd(array2)
    result = abs(cov / max_cov)

    if result > corr:
        return False
    else:
        return True


def mtcd_test3(date, row, col, dic_values, dic_mask, window_size, corr):

    dates_values = search_references_list(dic_values, dic_mask, row, col, "blue")[0]

    array_current_date = analysis_window(dic_values, date, row, col, window_size, edge='nan')
    arrays_previous_dates = []

    for date in dates_values:
        arrays_previous_dates.append(analysis_window(dic_values, date, row, col, window_size))

    correlations = []

    for array in arrays_previous_dates:
        correlations.append(cor_test3(array_current_date, array, corr))

    if False in correlations is True:
        return False
    else:
        return True

def mtcd(date, row, col, par1, par2, window_size, corr, dic_values, dic_mask):

    Test_1 = mtcd_test1(date, row, col, dic_values, dic_mask, par1)

    if Test_1 == -999:
        return -999

    if Test_1 is False:
        return True

    Test_2 = mtcd_test2(date, row, col, dic_values, dic_mask, par2)

    Test_3 = mtcd_test3(date, row, col, dic_values, dic_mask, window_size, corr)
    if Test_1 is True and Test_2 is True and Test_3 is True:
        return False
    else:
        return True






