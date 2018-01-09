import numpy as np

######## Search function example ###########

test_dic = {"date0": np.matrix([[0,0],[np.nan, np.nan]]), "date1": np.full((3, 3), 1, int),
            "date2":  np.full((3, 3), np.nan), "date3": np.full((3,3), 3, int), "date4": np.matrix([[np.nan,2],[3,4]])}

key_result = [key for key, value in test_dic.items() if key not in "date3"]
value_result = [value for key, value in test_dic.items() if key not in "date3"]
# extract all keys and values except the given one

pixel_values = [value[0,0] for value in value_result]
# extract a given row and column from the list

NA_values = np.isnan(pixel_values).tolist() # boolean list with True where np.nan
notNA_values = [not i for i in NA_values] # boolean list with True where different to np.nan

indices_notNA_values = [index for index, value in enumerate(notNA_values) if value == True]
# list of indices of the given list where the value is different from NA

index_reference_value = indices_notNA_values[-1]
# extracts the last value of the list, this will be the most recent not NA value we were looking for

reference_value= pixel_values[index_reference_value]
reference_date = key_result[index_reference_value]

###################################################################
test_dic = {"cero": np.matrix([[0,0],[np.nan, np.nan]]), "uno": np.full((3, 3), 1, int),
            "dos":  np.full((3, 3), np.nan), "tres": np.full((3,3), 3, int)}

def find_reference_date(dictionary, value):
    # prints all values that are not the one given in the parameter value
    for key, value in dictionary.items():
        if key not in value:
            print(key)

# why it doesn't work with return?

###################################################################

    def mtcd(date, row, col, par1, par2, size, corr, dic_values, dic_mask):
        """
        Run the multi temporal cloud detection test to identify if a pixel is cloud free or not.

        Run the three tests. For the third one, first search the reference value and date and define the two analysis
        windows in order to run the test 3. Check the result of the three tests and return np.nan for cloud pixels only if
        the first test returns true and the second and third false.

        :param str date: The date of the image.
        :param int row: The row of the pixel.
        :param int col: The column of the pixel.
        :param int size: The size of the analysis window.
        :param int par1: The percentage of variation in the blue band.
        :param int par2: The percentage of variation in the red band.
        :param int corr: The correlation coefficient above which True is returned.
        :param object dic_values: The dictionary with the dates and the pixel values of the image as arrays.
        :param object dic_mask: The dictionary with the dates and the cloud mask for the images.
        :return: np.nan if the pixel is a cloud and True if not.
        """

        Test_1 = mtcd_test1(date, row, col, dic_values, dic_mask, par1)

        if Test_1 == -999:
            return -999

        if Test_1 is False:
            return True

        Test_2 = mtcd_test2(date, row, col, dic_values, dic_mask, par2)

        reference_values = search_references_list(dic_values, dic_mask, row, col, "blue")[1]
        reference_dates = reference_values[0]

        array_current_date = analysis_window(dic_values, date, row, col, size, edge='nan')

        for i in reference_dates:
            array_reference_date = analysis_window(dic_values, reference_dates[i], row, col, size, edge='nan')

        Test_3 = cor_test3(array_current_date, array_reference_date, corr)

        if Test_1 is True and Test_2 is True and Test_3 is True:
            return False
        else:
            return True
