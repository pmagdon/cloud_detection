

def search_reference(dic_values, dic_mask, row, col, band_name):

    key_images = [key for key, value in dic_mask.items()]
    # extract the keys from the masked dictionary since these correspond to the dates previous to the given date

    value_images = [value for key, value in dic_values[band_name].items() if key in key_images]
    # extract the values corresponding to the dates in key result, these are the values of all the images taken before
    # the given date

    mask_images = [value for key, value in dic_mask.items() if key in key_images]
    # extract the masked value (1 for not cloud and na for cloud) for the images taken before the given date

    mask_pixel = [value[row, col] for value in mask_images]
    # extract the masked values for a given row and column in all images taken before the given date

    value_pixel = [value[row, col] for value in value_images]
    # extract the values for a given row and column in all images taken before the given date

    indices_not_cloud = [index for index, value in enumerate(mask_pixel) if value == 1]
    # extract the indices from the list "mask_pixel" that are True, i.e. that are cloud free

    index_recent_not_cloud = indices_not_cloud[-1]
    # extract the last value of the list of "indices_not_cloud", i.e. the index of the most recent not cloud value

    reference_date = key_images[index_recent_not_cloud]
    reference_value = value_pixel[index_recent_not_cloud]

    return reference_date, reference_value
