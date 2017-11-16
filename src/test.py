import numpy as np

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
