from src.multi_temporal_cloud_detection import mtcd

import numpy as np


def cloud_mask(dic, date, cloud_mask_dic):
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

    cloud_mask_dic.update({date: cloud_mask_array})
    print("Cloud mask dictionary updated")
