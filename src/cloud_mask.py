from src.multi_temporal_cloud_detection import mtcd
import numpy as np
from src.main import *


def cloud_mask(date, window_size, dic_mask=dictionary_masked):
    """

    :param date:
    :param window_size:
    :param dic_mask:
    :return:
    """
    nrow = dictionary_blue_red["blue"][date].shape[0]
    ncol = dictionary_blue_red["blue"][date].shape[1]

    cloud_mask_list = [mtcd(date, r, c, 3)
                       for r in range(0, nrow)
                       for c in range(0, ncol)]

    cloud_mask_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)

    dic_mask.update({date: cloud_mask_array})

    print("Dictionary masked updated")


    """
    Run the mtcd test for all the pixels of an image of a given date and update the cloud mask dictionary.

    Args:
        dic(object): the dictionary with the images and their values (dictionary_blue_red)
        date (str): the date of the image
        cloud_mask_dic (object): dictionary thatcontains the date of the image and the cloud mask with np.nan
            for cloud pixels and True for not cloud pixels


    Returns:
        blsblsbslb
    """

