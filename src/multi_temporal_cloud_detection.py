import datetime
import math
import numpy as np
from src.search_reference import search_reference


## Test 1 ##
def blue_test(date, row, col, dic_values, dic_mask, blue_par):
    """
    Test the temporal variation of reflectance on the blue band comparing it to a threshold. A big increase (True)
    indicates cloud.

    Extract the most recent cloud free pixel value of the blue band and its corresponding date to a list. Extract the
    current blue reflectance value of the pixel using the current date as the key of the dictionary. The pixel is defined by
    its row and column in the array representing the image.

    Calculate the mean reflectance using all the pixels of the reference and current image. Calculate the ratio between
    these two means and if this ratio is beyond 1.5 or under 0.5, increase the blue parameter value multiplying by 1.5.

    Compare the variation between the current pixel value and the cloud-free reference value with a threshold given by
    the blue parameter. The value of this parameter depends on the time interval between the two images:
    if the images are close in time the parameter doesn't change very much, but if there are 30 days between the
    acquisition time of the two images, the parameter doubles its value.

    If the pixel value variation is bigger than the threshold, classify the pixel as cloudy (True) and if not, as cloud
    free (False).

    :param str date: The date of the image which is currently analysed.
    :param int row: The row of the image for a pixel.
    :param int col: The column of the image for a pixel.
    :param object dic_values: The dictionary with the dates and the pixel values of the image saved as arrays.
    :param object dic_mask: The dictionary with the dates and the generated cloud mask for the already analysed images.
    :param int blue_par: The percentage of reflectance variation in the blue band used as threshold.
    :return: True if the reflectance variation is bigger than a threshold (cloudy pixel), False if it is not (cloud free
             pixel), -999 if the current pixel value is np.nan.
    """

    reference = search_reference(dic_values, dic_mask, row, col, "blue")

    date_ref = datetime.datetime.strptime(reference[0], "%Y-%m-%d")
    value_ref = reference[1]

    current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    current_value = dic_values["blue"][date][row, col]

    if math.isnan(current_value) is False:
        current_value_mean = np.nanmean(dic_values["blue"][date])
        ref_value_mean = np.nanmean(dic_values["blue"][reference[0]])
        if current_value_mean / ref_value_mean > 1.5 or current_value_mean / ref_value_mean < 0.5:
            blue_par *= 1.5

    if math.isnan(current_value) is True:
        return -999
    elif current_value - value_ref > blue_par * (
        1 + (current_date - date_ref).total_seconds() / (60 * 60 * 24) / 30):
        return True
    else:
        return False


# Test 2 #

def red_blue_test(date, row, col, dic_values, dic_mask, red_blue_par):
    """
    Test the temporal variation of reflectance in the red band in comparison with the variation in the blue band. A
    bigger variation in the red band (True) indicates cloud free pixel.

    Extract the reflectance value from the most recent cloud free pixel of the blue and of the red band.  Extract the
    reflectance value from the current pixel of the blue and of the red band. Calculate the temporal variation
    between the reference and the current value for both bands and compare this variation. If the temporal variation
    in the red band is over the temporal variation in the blue band multiplied by the blue band parameter, return True.

    :param  str date: The date of the image which is currently analysed.
    :param int row: The row of the image for a pixel.
    :param int col: The column of the image for a pixel.
    :param object dic_values: The dictionary with the dates and the pixel values of the image saved as arrays.
    :param object dic_mask: The dictionary with the dates and the generated cloud mask for the already analysed images.
    :param int red_blue_par: The percentage of reflectance variation between the red and the blue band used as the threshold.
    :return: True if the temporal variation in the red band reflectance is bigger than in the blue band (cloud free
             pixel) and False if it is not (cloudy pixel).

    """
    ref_blue = search_reference(dic_values, dic_mask, row, col, "blue")
    ref_red = search_reference(dic_values, dic_mask, row, col, "red")

    value_ref_red = ref_red[1]
    current_value_red = dic_values["red"][date][row, col]

    value_ref_blue = ref_blue[1]
    current_value_blue = dic_values["blue"][date][row, col]

    if (current_value_red - value_ref_red) > red_blue_par * (current_value_blue - value_ref_blue):
        return True
    else:
        return False


def analysis_window(dic, date, row, col, window_size, edge='nan'):
    """
    Extract the values within an analysis window from an 2D-array.

    The location in the image array of the pixel for which the window is extracted is defined by the parameters row and
    col. This is the central pixel of the square-shaped window. Therefore, the sides of the window need to be odd.
    Place a NAN edge around the image. The width of this edge corresponds to the floor of half of the size of the
    window. This makes possible to extract the values placed at the edge of the image. The creation of the NAN edge
    modifies the indexing, therefore adjust the row and the column values by adding the floor of half of a window's
    size. Extract from the image array with added edges the values within the analysis window as an array.

    :param object dic: The dictionary with the dates and the pixel values of the image saved as arrays.
    :param str date: The date of the image which is currently analysed.
    :param int row: The row of the image for a pixel.
    :param int col: The column of the image for a pixel.
    :param int window_size: The size of a side of the analysis window, needs to be odd.
    :param str edge: The value of the edge of the image.
    :return: The window as an array with the pixel reflectance values and nan values in the case that is over the limits of
             the image.
    """

    if window_size % 2 == 0:
        raise ValueError(" Size needs to be odd")
    if edge != 'nan':
        raise ValueError(" Edge argument needs to be 'nan'")

    half_window = math.floor(window_size / 2)

    row_adjusted = row + half_window
    col_adjusted = col + half_window

    array = dic["blue"][date]
    array_with_margins = np.pad(array.astype(float), pad_width=half_window, mode='constant', constant_values=np.nan)
    result = array_with_margins[row_adjusted - half_window:row_adjusted + half_window + 1,
                                col_adjusted - half_window:col_adjusted + half_window + 1]

    return result


def cor_array(array_current_date, array_reference_date, cor_coeff):
    """
    Calculate the correlation coefficient between two arrays and return True if the value is over a threshold.

    Calculate the actual covariance and the maximal covariance between two arrays storing the reflectance values of a
    central pixel and its neighbourhood. One array corresponds to the current pixel and the second one to the reference
    pixel. Divide between the covariance and the maximal covariance to get the correlation coefficient. If this
    value is above the value of the parameter correlation coefficient, return True.

    :param array_current_date: The array storing the reflectance values of the current pixel and its neighbourhood.
    :param array_reference_date: The array storing the reflectance values of the reference pixel and its neighbourhood.
    :param cor_coeff: The correlation coefficient used as a threshold.
    :return: True if the calculated coefficient is bigger than the parameter (not cloud) and False if it is not (cloud).
    """
    cov = np.nanmean((array_current_date - np.nanmean(array_current_date)) *
                     (array_reference_date - np.nanmean(array_reference_date)))
    max_cov = np.nanstd(array_current_date) * np.nanstd(array_reference_date)
    result = abs(cov / max_cov)

    if result > cor_coeff:
        return True
    else:
        return False


def neigh_cor(date, row, col, dic_values, dic_mask, window_size, cor_coeff):
    """
    Calculate the correlation coefficient between an array and other 10 arrays and return True if any of these
    correlation coefficients is above a given threshold.

    Save the dates of the last 10 images previous to the date of the current analysed image. Use the analysis_window()
    function to extract 11 arrays storing reflection value of the pixel and its neighbourhood. One array corresponds to
    the pixel of the current date and the other 10 to the same pixel in the ten previous images. Use the cor_test3()
    function to test if any of the ten calculated correlation coefficients between the array of the current date and the
    other ten arrays of the previous dates is above the correlation coefficient parameter. If this is the case, return
    True, else return False.

    :param date: The date of the image which is currently analysed.
    :param row: The row of the image for a pixel.
    :param col: The column of the image for a pixel.
    :param dic_values: The dictionary with the dates and the pixel values of the image saved as arrays.
    :param dic_mask: The dictionary with the dates and the generated cloud mask for the already analysed images.
    :param window_size: The size of a side of the analysis window, needs to be odd.
    :param cor_coeff: The correlation coefficient used as a threshold.
    :return: True if any of the 10 calculated correlations between the current and the previous arrays is bigger than
             the threshold correlation coefficient parameter (not cloud) and False if none of them is above the
             parameter (cloud).
    """
    # dates_values = search_references_list(dic_values, dic_mask, row, col, "blue")[0]

    dates_values = [key for key, value in dic_mask.items()][-10:]

    array_current_date = analysis_window(dic_values, date, row, col, window_size, edge='nan')
    arrays_previous_dates = []

    for date in dates_values:
        arrays_previous_dates.append(analysis_window(dic_values, date, row, col, window_size))

    correlations = []

    for array_reference_date in arrays_previous_dates:
        correlations.append(cor_array(array_current_date, array_reference_date, cor_coeff))

    if True in correlations:
        return True
    else:
        return False


def mtcd(date, row, col, blue_par, red_blue_par, window_size, cor_coef, dic_values, dic_mask, test_version):
    """
    Run the multi temporal cloud detection test to identify if a pixel is cloud free or not.

    If the test_version parameter is 0:
    Run the blue band test. If the blue band test returns -999, return -999; if it returns False (no high temporal
    variation in the blue band), return True (pixel is not a cloud); if it returns True (high temporal variation in the
    blue band), run the red-blue band test and the correlation test and only if both return False (no high temporal
    variation in the red band and no high correlation between images neighbourhood), return True (pixel tagged as cloudy).
    If the test_version parameter is 1:
    Run the same procedure, but return 3 results, each one for each of the results of the 3 tests. If only the blue band
    test is run, return three times this result.

    :param str date: The date of the image which is currently analysed.
    :param int row: The row of the image for a pixel.
    :param int col: The column of the image for a pixel.
    :param int window_size: The size of a side of the analysis window, needs to be odd.
    :param int blue_par: The percentage of reflectance variation in the blue band used as threshold.
    :param int red_blue_par: The percentage of reflectance variation between the red and the blue band used as a threshold.
    :param int cor_coef: The correlation coefficient used as a threshold.
    :param object dic_values: The dictionary with the dates and the pixel values of the image saved as arrays.
    :param object dic_mask: The dictionary with the dates and the generated cloud mask for the already analysed images.
    :return: With test version equal 0: -999 if the blue test is -999 (no data), True if the blue test is False or if
             the blue test is True but one of the other two tests is True (no cloud), False if the blue test is True and
             the other two tests are False (cloud).
             With test version equal 1: Return the results of the three tests or of the first test three times.
    """

    test_blue = blue_test(date, row, col, dic_values, dic_mask, blue_par)

    if test_version == 0:
        if test_blue == -999:
            return -999
        elif test_blue is False:
            return True  # not cloud
        elif test_blue is True:
            test_red_blue = red_blue_test(date, row, col, dic_values, dic_mask, red_blue_par)
            neighb_test = neigh_cor(date, row, col, dic_values, dic_mask, window_size, cor_coef)
            if test_blue is True and test_red_blue is False and neighb_test is False:
                return False
            else:
                return True

    elif test_version == 1:
        if test_blue == -999:
            return test_blue, -999, -999
        elif test_blue is False:
            return False, -999, -999
        elif test_blue is True:
            test_red_blue = red_blue_test(date, row, col, dic_values, dic_mask, red_blue_par)
            neighb_test = neigh_cor(date, row, col, dic_values, dic_mask, window_size, cor_coef)
            return test_blue, test_red_blue, neighb_test


