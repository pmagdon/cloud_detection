
def search_reference(dic_values, dic_mask, row, col, band_name):
    """
    Search and return the most recent cloud free value of the time series and its date before the current date.

    Extract all dates previous to the date of the current analysed image by accessing the keys from the masked
    dictionary. For these dates, extract the pixel value from the values dictionary and the masked value from the masked
    dictionary for a given pixel and write them in two different lists.
    Extract the indices of the cloud free pixels in a new list and from this indices list, save the last value. This
    index corresponds to the most recent cloud free value and is used in the next step to subset the most recent cloud
    free date and pixel value.

    :param object dic_values: The dictionary with the dates and the pixel values of the image saved as arrays.
    :param object dic_mask: The dictionary with the dates and the generated cloud mask for the already analysed images.
    :param int row: The row of the image for a pixel.
    :param int col: The column of the image for a pixel.
    :param str band_name: The band from which the pixel values are extracted.
    :return: A list with the most recent cloud free date and pixel value.
    """
    key_images = [key for key, value in dic_mask.items()]

    value_pixel = [value[row,col] for key, value in dic_values[band_name].items() if key in key_images]
    mask_pixel = [value[row,col] for key, value in dic_mask.items() if key in key_images]

    indices_not_cloud = [index for index, value in enumerate(mask_pixel) if value == 1][-1]

    reference_date = key_images[indices_not_cloud]
    reference_value = value_pixel[indices_not_cloud]

    return reference_date, reference_value