import datetime
import math
import numpy as np
from src.search_reference import search_references_list


## Test 1 ##
def mtcd_test1(date, row, col, dic_values, dic_mask, par1):
    """
    Test the temporal variation of reflectance on the blue band comparing it to a threshold. A big increase (True)
    indicates cloud.

    To compare the pixel values of the current image with the reference values, first extract the most recent cloud
    free pixel value an corresponding date to a list with the search_reference function. Extract the current blue band
    reflectance value of the pixel using the current date as key. The pixel is defined by its location in the image
    through the parameters row and column.

    Calculate the mean reflectance for the whole reference and current image. Calculate the ratio between these two
    means and if this ratio is beyond 1.5 or under 0.5, increase the blue parameter value multiplying by 1.5.

    Compare the variation between the current pixel value and the cloud free reference value with a threshold given by
    the blue parameter. This parameter is a function of the time interval between the two images:
    if the images are close in time the parameter doesn't change very much, but if there are 30 days between the
    acquisition time of the two images, the parameter doubles its value.

    If the pixel value variation is bigger than the threshold, classify the pixel as cloud (True) and if not, as cloud
    free (False).

    :param str date: The date of the image which is currently analysed.
    :param int row: The row of the image for a pixel.
    :param int col: The column of the image for a pixel.
    :param object dic_values: The dictionary with the dates and the pixel values of the image saved as arrays.
    :param object dic_mask: The dictionary with the dates and the generated cloud mask for the already analysed images.
    :param int par1: The percentage of reflectance variation in the blue band for comparision.
    :return: True if cloudy pixel, False if cloud free pixel
    """

    reference = search_references_list(dic_values, dic_mask, row, col, "blue")

    date_ref = datetime.datetime.strptime(reference[0][-1], "%Y-%m-%d")
    value_ref = reference[1][-1]

    current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    current_value = dic_values["blue"][date][row, col]

    current_value_mean = np.nanmean(dic_values["blue"][date])
    ref_value_mean = np.nanmean(dic_values["blue"][reference[0][-1]])
    if current_value_mean / ref_value_mean > 1.5 or current_value_mean / ref_value_mean < 0.5:
        par1 *= 1.5

    if math.isnan(current_value) is True:
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
    ref_blue = search_references_list(dic_values, dic_mask, row, col, "blue")
    ref_red = search_references_list(dic_values, dic_mask, row, col, "red")

    value_ref_red = ref_red[1][-1]
    current_value_red = dic_values["red"][date][row, col]

    value_ref_blue = ref_blue[1][-1]
    current_value_blue = dic_values["blue"][date][row, col]

    if (current_value_red - value_ref_red) > par2 * (current_value_blue - value_ref_blue):
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

    if size % 2 == 0:
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


def cor_test3(array_current_date, array_reference_date, cor_coeff):
    """

    :param array_current_date:
    :param array_reference_date:
    :param cor_coeff:
    :return:
    """
    cov = np.nanmean((array_current_date - np.nanmean(array_current_date)) *
                     (array_reference_date - np.nanmean(array_reference_date)))
    max_cov = np.nanstd(array_current_date) * np.nanstd(array_reference_date)
    result = abs(cov / max_cov)

    if result > cor_coeff:
        return True
    else:
        return False


def mtcd_test3(date, row, col, dic_values, dic_mask, window_size, cor_coeff):
    """
    Save the dates of the 10 most recent dates of pixels that are cloud free. Use the analysis_window function to
    extract the pixel neighbourhood values within an analysis window for the 10 most recent cloud free pixels
    (array_previous_dates) as well as for the pixel value from the current date (array_current_date). Use the cor_test3
    function to test if any of the correlations between array_current date and each of the arrays in the list
    arrays_previous_dates is above a certain correlation coefficient. If this is the case, return True, else return
    False.

    :param date:
    :param row:
    :param col:
    :param dic_values:
    :param dic_mask:
    :param window_size:
    :param cor_coeff:
    :return:
    """
    #dates_values = search_references_list(dic_values, dic_mask, row, col, "blue")[0]

    dates_values = [key for key, value in dic_mask.items()][-10:]

    array_current_date = analysis_window(dic_values, date, row, col, window_size, edge='nan')
    arrays_previous_dates = []

    for date in dates_values:
        arrays_previous_dates.append(analysis_window(dic_values, date, row, col, window_size))

    correlations = []

    for array_reference_date in arrays_previous_dates:
        correlations.append(cor_test3(array_current_date, array_reference_date, cor_coeff))

    if True in correlations:
        return True
    else:
        return False


def mtcd(date, row, col, par1, par2, window_size, cor_coef, dic_values, dic_mask, test_version):
    """
    Run the multi temporal cloud detection test to identify if a pixel is cloud free or not.

    Run the three tests. For the third one, first search the reference value and date and define the two analysis
    windows in order to run the test 3. Check the result of the three tests and return np.nan for cloud pixels only if
    the first test returns true and the second and third false.

    :param str date: The date of the image.
    :param int row: The row of the pixel.
    :param int col: The column of the pixel.
    :param int window_size: The size of the analysis window.
    :param int par1: The percentage of variation in the blue band.
    :param int par2: The percentage of variation in the red band.
    :param int cor_coef: The correlation coefficient above which True is returned.
    :param object dic_values: The dictionary with the dates and the pixel values of the image as arrays.
    :param object dic_mask: The dictionary with the dates and the cloud mask for the images.
    :return: np.nan if the pixel is a cloud and True if not.
    """

    Test_1 = mtcd_test1(date, row, col, dic_values, dic_mask, par1)

    if test_version == 0:
        if Test_1 == -999:
            return -999
        elif Test_1 is False:
            return True  # not cloud
        elif Test_1 is True:
            Test_2 = mtcd_test2(date, row, col, dic_values, dic_mask, par2)
            Test_3 = mtcd_test3(date, row, col, dic_values, dic_mask, window_size, cor_coef)
            if Test_1 is True and Test_2 is False and Test_3 is False:
                return False
            else:
                return True

    elif test_version == 1:
        if Test_1 == -999:
            return Test_1, -999, -999
        elif Test_1 is False:
            return False, -999, -999
        elif Test_1 is True:
            Test_2 = mtcd_test2(date, row, col, dic_values, dic_mask, par2)
            Test_3 = mtcd_test3(date, row, col, dic_values, dic_mask, window_size, cor_coef)
            return Test_1, Test_2, Test_3


