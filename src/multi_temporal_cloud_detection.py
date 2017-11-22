import datetime
import math
#from src.search_reference import search_reference
#from src.main import *

# Test 1 #
def mtcd_test1(date, row, col, dic_values = dictionary_blue_red, dic_mask = dictionary_masked):
    # test if the temporal variation of reflectance on the blue band is big compared to a threshold
    # Big increase indicates cloud

    reference_values = search_reference(dic_values, dic_mask, row, col, "blue")

    date_ref = datetime.datetime.strptime(reference_values[0], "%Y-%m-%d") # extracts the pixel value of an image
    value_ref = reference_values[1]  # extracts the pixel value of the reference image

    current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    current_value = dic_values["blue"][date][row, col]

    if current_value - value_ref > 3 * (
        1 + (current_date - date_ref).total_seconds() / (60 * 60 * 24) / 30):
        return True
    else:
        return False


# Test 2 #
def mtcd_test2(date, row, col, dic_values = dictionary_blue_red, dic_mask = dictionary_masked):
    # test if the variation of reflectance in the red band is much greater than in the blue band

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

def mtcd(date, row, col, size, dic_values = dictionary_blue_red, dic_mask = dictionary_masked):
    # check the result of the 3 tests and returns
    # True when cloud, False when not cloud

    Test_1 = mtcd_test1(date, row, col, dic_values, dic_mask)
    Test_2 = mtcd_test2(date, row, col, dic_values, dic_mask)
    reference_values = search_reference(dic_values, dic_mask, row, col, "blue")
    date_ref = reference_values[0]

    array_current_date = moving_window(dic_values, date, row, col, size, edge='nan')
    array_reference_date = moving_window(dic_values, date_ref, row, col, size, edge='nan')
    Test_3 = cor_test3(array_current_date, array_reference_date)
    if Test_1 == True and Test_2 == False and Test_3 == False:
        return np.nan
    else:
        return True




