import datetime
import math
import numpy as np
from src.search_reference import search_reference


def mtcd_test1(date, row, col, dic_values, dic_mask):
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
    :return: True if cloudy pixel, False if cloud free pixel
    """

    reference_values = search_reference(dic_values, dic_mask, row, col, "blue")

    date_ref = datetime.datetime.strptime(reference_values[0], "%Y-%m-%d")
    value_ref = reference_values[1]

    current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    current_value = dic_values["blue"][date][row, col]

    if current_value - value_ref > 3 * (
        1 + (current_date - date_ref).total_seconds() / (60 * 60 * 24) / 30):
        return True
    else:
        return False


# Test 2 #
def mtcd_test2(date, row, col, dic_values, dic_mask):
    """
    Test the temporal variation of reflectance on the red band comparing it to a threshold which is a function of the
    time interval. A big increase (True) indicates cloud.

    To compare the values of the image with the most recent cloud free reference, first extract the reference values
    (date and pixel value) to a list with the search_reference function. Extract the current values of the red band
    for the selected pixel defined by its row and its column (parameters) from the values dictionary using as key the
    given date parameter. Compare the variation between the current pixel value and the cloud free reference value with
    a threshold that is a function of the time interval between the two images. If the pixel value variation is bigger
    than the threshold, classify the pixel as cloud free (True) and if not, as cloud (False).

    :param str date: The date of the image which is analysed at the moment.
    :param int row: The row of the pixel.
    :param int col: The column of the pixel.
    :param object dic_values: The dictionary with the dates and the pixel values of the image as arrays.
    :param object dic_mask: The dictionary with the dates and the cloud mask for the images.
    :return: True if cloud free pixel, False if cloudy pixel
    """

    reference_values = search_reference(dic_values, dic_mask, row, col, "red")

    date_ref = datetime.datetime.strptime(reference_values[0], "%Y-%m-%d") # extracts the pixel value of an image
    value_ref = reference_values[1]  # extracts the pixel value of the reference image

    current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    current_value = dic_values["red"][date][row, col]

    if current_value - value_ref > 150 * (
                1 + (current_date - date_ref).total_seconds() / (60 * 60 * 24) / 30):
        return True
    else:
        return False


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
        raise ValueError(" Edge argument needs to of 'nan', ...")

    half_window = math.floor(size / 2)

    row_adjusted = row + half_window
    col_adjusted = col + half_window

    array = dic["blue"][date]
    array_with_margins = np.pad(array.astype(float), pad_width=half_window, mode='constant', constant_values=np.nan)
    result = array_with_margins[row_adjusted - half_window:row_adjusted + half_window + 1,
                                col_adjusted - half_window:col_adjusted + half_window + 1]

    return result


def cor_test3(array1, array2):
    """
    Calculate the correlation between two arrays and return True if this is above 50%.

    :param object array1: The first array.
    :param object array2: The second array.
    :return: True if the correlation is above 50% and False if not.
    """
    cov = np.nanmean((array1 - np.nanmean(array1)) * (array2 - np.nanmean(array2)))
    max_cov = np.nanstd(array1) * np.nanstd(array2)
    result = abs(cov / max_cov)
    if result > 0.5:
        return True
    else:
        return False


def mtcd(date, row, col, size, dic_values, dic_mask):
    """
    Run the multi temporal cloud detection test to identify if a pixel is cloud free or not.

    Run the three tests. For the third one, first search the reference value and date and define the two analysis
    windows in order to run the test 3. Check the result of the three tests and return np.nan for cloud pixels only if
    the first test returns true and the second and third false.

    :param str date: The date of the image.
    :param int row: The row of the pixel.
    :param int col: The column of the pixel.
    :param int size: The size of the analysis window.
    :param object dic_values: The dictionary with the dates and the pixel values of the image as arrays.
    :param object dic_mask: The dictionary with the dates and the cloud mask for the images.
    :return: np.nan if the pixel is a cloud and True if not.
    """

    Test_1 = mtcd_test1(date, row, col, dic_values, dic_mask)
    Test_2 = mtcd_test2(date, row, col, dic_values, dic_mask)

    reference_values = search_reference(dic_values, dic_mask, row, col, "blue")
    date_ref = reference_values[0]

    array_current_date = analysis_window(dic_values, date, row, col, size, edge='nan')
    array_reference_date = analysis_window(dic_values, date_ref, row, col, size, edge='nan')

    Test_3 = cor_test3(array_current_date, array_reference_date)

    if Test_1 == True and Test_2 == False and Test_3 == False:
        return np.nan
    else:
        return True




