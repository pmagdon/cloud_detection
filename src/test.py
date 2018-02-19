import numpy as np

######## Search function example ###########

test_dic = {"date0": np.matrix([[0,0],[np.nan, np.nan]]), "date1": np.full((3, 3), 1, int),
            "date2":  np.full((3, 3), np.nan), "date3": np.full((3,3), 3, int), "date4": np.matrix([[np.nan,2],[3,4]])}

#for date in dictionary_blue_red["blue"].keys():
#    print(date + str(": ") + str(np.mean(dictionary_blue_red["blue"][date])))


################# only test 1 ############################

def only_test1(date, dic_values, dic_mask, par1):
    nrow = dic_values["blue"][date].shape[0]
    ncol = dic_values["blue"][date].shape[1]

    cloud_mask_list = []

    for r in range(0, nrow):
        for c in range(0, ncol):
            cloud_mask_list.append(mtcd_test1(date, r, c, dic_values, dic_mask, par1))

    cloud_mask_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)

    dic_mask.update({date: cloud_mask_array})

    print("Dictionary masked of date %s updated"%(date))

for date in list(dictionary_blue_red["blue"].keys())[1:]:
    only_test1(date, dictionary_blue_red, dictionary_masked, 3)

################# only test 3 #######################


def only_test3(date, dic_values, dic_mask, window_size, cor_coeff):
    nrow = dic_values["blue"][date].shape[0]
    ncol = dic_values["blue"][date].shape[1]

    cloud_mask_list = []

    for r in range(0, nrow):
        for c in range(0, ncol):
            cloud_mask_list.append(mtcd_test3(date, r, c, dic_values, dic_mask, window_size, cor_coeff))

    cloud_mask_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)

    dic_mask.update({date: cloud_mask_array})

    print("Dictionary masked of date %s updated"%(date))

for date in list(dictionary_blue_red["blue"].keys())[1:]:
    only_test3(date, dictionary_blue_red, dictionary_masked, 7, 0.55)

#### old search reference function ####

# cloud_mask("2015-05-15", 1.5, 1.5, 13, 0.55, dictionary_blue_red, dictionary_masked)
# array2raster("data/2015-03-19.tif", 'cm_2015-03-19.tiff', 5, 5, dictionary_masked, "2015-03-19")


#def search_reference(dic_values, dic_mask, row, col, band_name):
#    """
#    Search and return the most recent cloud free value of the time series and its date before the current date.
#
#    Extract all dates previous to the date of the current analysed image by accessing the keys from the masked
#    dictionary, which contains the cloud masks for the images analysed until the moment. For these dates, extract
#    all the pixel values as well as all the masked values in form of arrays, the first ones from the values dictionary
#    and the second ones from the masked dictionary. The masked values are 1 if the pixel is not a cloud and 0 if it is
#    a cloud. From these arrays, extract the pixel values and the masked values for a given pixel in two different
#    lists. Extract the indices of the cloud free pixels of the second list (masked values) in a new list and from
#    this indices list, save the last value. This index corresponds to the most time recent cloud free value and is
#    used in the next step to subset the most recent cloud free date and pixel value.

#    :param object dic_values: The dictionary with the dates and the pixel values of the image as arrays.
#    :param object dic_mask: The dictionary with the dates and the cloud mask for the images.
#    :param int row: The row of the pixel.
#    :param int col: The column of the pixel.
#    :param str band_name: The band from which the pixel values are extracted.
#    :return: A list with the most recent cloud free date and pixel value.
#    """
#    key_images = [key for key, value in dic_mask.items()]

#    value_images = [value for key, value in dic_values[band_name].items() if key in key_images]
#    mask_images = [value for key, value in dic_mask.items() if key in key_images]

#    mask_pixel = [value[row, col] for value in mask_images]
#    value_pixel = [value[row, col] for value in value_images]

#    indices_not_cloud = [index for index, value in enumerate(mask_pixel) if value == 1]

#    index_recent_not_cloud = indices_not_cloud[-1]

#    reference_date = key_images[index_recent_not_cloud]
#   reference_value = value_pixel[index_recent_not_cloud]

#    return reference_date, reference_value