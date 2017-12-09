from src.multi_temporal_cloud_detection import mtcd
import numpy as np

def cloud_mask(date, par1, par2, size, corr, dic_values, dic_mask):
    """
    Create a cloud mask from an image and put it in the corresponding dictionary.

    Get the number of rows and of columns from an image, run the multi temporal cloud detection test with help of the
    mtcd function for all the pixels of the image of a given date and update the cloud mask dictionary.

    :param str date: the date of the image
    :param int size: the size of the window for the part 3 of the multi temporal cloud detection test
    :param object dic_values: The dictionary with the dates and the pixel values of the image as arrays.
    :param object dic_mask: dictionary that contains the date of the image and the cloud mask with np.nan for cloud
            pixels and True for not cloud pixels
    :return: Print the message "Dictionary masked updated".
    """
    nrow = dic_values["blue"][date].shape[0]
    ncol = dic_values["blue"][date].shape[1]

    cloud_mask_list = [mtcd(date, r, c, par1, par2, size, corr, dic_values, dic_mask)
                       for r in range(0, nrow)
                       for c in range(0, ncol)]

    cloud_mask_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)

    dic_mask.update({date: cloud_mask_array})

    print("Dictionary masked updated")

