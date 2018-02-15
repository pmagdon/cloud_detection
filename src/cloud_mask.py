from src.multi_temporal_cloud_detection import mtcd, mtcd_test1
import numpy as np
#from tqdm import tqdm


def cloud_mask(date, par1, par2, size, corr, dic_values, dic_mask, test_version, dic_mask_test = "foo"):
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

    total = nrow*ncol
    #pbar = tqdm.tqdm(total=total)

    cloud_mask_list = []
    cm_list_test1 = []
    cm_list_test2 = []
    cm_list_test3 = []

    if test_version == 0:

        for r in range(0, nrow):
            for c in range(0, ncol):
                cloud_mask_list.append(mtcd(date, r, c, par1, par2, size, corr, dic_values, dic_mask, 0))
                #pbar.update(1)
        #pbar.close()

        cm_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)

        dic_mask.update({date: cm_array})
        print("Dictionary masked of date %s updated" % (date))

    if test_version == 1:

        for r in range(0,nrow):
            for c in range(0,ncol):
                cm_list_test1.append(mtcd(date, r, c, par1, par2, size, corr, dic_values, dic_mask, 1)[0])
                cm_list_test2.append(mtcd(date, r, c, par1, par2, size, corr, dic_values, dic_mask, 1)[1])
                cm_list_test3.append(mtcd(date, r, c, par1, par2, size, corr, dic_values, dic_mask, 1)[2])
                cloud_mask_list.append(mtcd(date, r, c, par1, par2, size, corr, dic_values, dic_mask, 0))

        cm_array1 = np.asarray(cm_list_test1).reshape(nrow, ncol)
        cm_array2 = np.asarray(cm_list_test2).reshape(nrow, ncol)
        cm_array3 = np.asarray(cm_list_test3).reshape(nrow, ncol)
        cm_array_3d = np.array([cm_array1, cm_array2, cm_array3])
        dic_mask_test.update({date: cm_array_3d})

        cm_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)
        dic_mask.update({date: cm_array})
        print("Both masked dictionaries of date %s updated" % (date))



