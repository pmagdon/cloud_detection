from src.multi_temporal_cloud_detection import mtcd
import numpy as np


def cloud_mask(dic, date, cloud_mask_dic):
    # runs the mtcd test for all the pixels of an image of a given date
    # dic is the dictionary with the images and their values (dictionary_blue_red)
    # output: cloud_mask_dic is the dictionary that is updated when running this function
    # cloud_mask_dic contains the date of the image and the cloud mask with np.nan
    # for cloud pixels and True for not cloud pixels
    nrow = dic["blue"][date].shape[0]
    ncol = dic["blue"][date].shape[1]
    cloud_mask_list = [mtcd(dic, "blue", r, c, date)
        for r in range(0, nrow)
        for c in range(0, ncol)]
    cloud_mask_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)
    cloud_mask_dic.update({date: cloud_mask_array})
    print("Cloud mask dictionary updated")
