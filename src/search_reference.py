

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

def search_references_list(dic_values, dic_mask, row, col, band_name):
    """
    Search and return the most recent cloud free value of the time series and its date before the current date.

    Extract all dates previous to the date of the current analysed image by accessing the keys from the masked
    dictionary, which contains the cloud masks for the images analysed until the moment. For these dates, extract
    all the pixel values as well as all the masked values in form of arrays, the first ones from the values dictionary
    and the second ones from the masked dictionary. The masked values are 1 if the pixel is not a cloud and 0 if it is
    a cloud. From these arrays, extract the pixel values (value_pixel) and the masked values (mask_pixel) for a given
    pixel in two different lists. Select the indices of the cloud free pixels of the mask_pixel list and extract them
    in a new list (indices_not_cloud). Use this list to select the dates and the values which are cloud free. From these
    values, select only the 10 last, which correspond to the 10 most recent values and save them in two lists
    (data_cloudfree and values_cloudfree).

    :param dic_values: The dictionary with the dates and the pixel values of the image as arrays.
    :param dic_mask: The dictionary with the dates and the cloud mask for the images.
    :param row: The row of the pixel.
    :param col: The column of the pixel.
    :param band_name: The band from which the pixel values are extracted.
    :return: A list with the 10 last cloud free date and pixel values.
    """
    key_images = [key for key, value in dic_mask.items()]

    value_images = [value for key, value in dic_values[band_name].items() if key in key_images]
    mask_images = [value for key, value in dic_mask.items() if key in key_images]

    mask_pixel = [value[row, col] for value in mask_images]
    value_pixel = [value[row, col] for value in value_images]

    indices_not_cloud = [index for index, value in enumerate(mask_pixel) if value == 1][-10:]

    data_cloudfree = [key_images[i] for i in indices_not_cloud]
    values_cloudfree = [value_pixel[i] for i in indices_not_cloud]

    return data_cloudfree, values_cloudfree

