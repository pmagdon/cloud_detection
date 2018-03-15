from src.multi_temporal_cloud_detection import mtcd
import numpy as np
#from tqdm import tqdm


def cloud_mask(date, blue_par, red_blue_par, window_size, cor_coeff, dic_values, dic_mask, test_version, dic_mask_test ="foo"):
    """
    Create a cloud mask from an image and put it in the corresponding dictionary.

    Get the number of rows and of columns from an image, run the multi-temporal cloud detection function for all the
    pixels of the image of a given date and store the results into a list. Reshape this list into an array of the shape
    of the image and update the corresponding cloud mask dictionary with this array for the current date. If the test
    version is activated, the return of the multi-temporal cloud detection function will be three values and they will
    be stored in three lists, each one of them corresponding to each test. Reshape each of the three lists into three
    arrays of the shape of the image and use them to create a 3D array. Update the test masked dictionary with this
    3D array and also update the standard masked dictionary with the standard cloud mask.

    :param str date: The date of the image which is currently analysed.
    :param int window_size: The size of a side of the analysis window, needs to be odd.
    :param object dic_values: The dictionary with the dates and the pixel values of the image saved as arrays.
    :param object dic_mask: The dictionary with the dates and the generated cloud mask for the already analysed images.
    :param bool test_version: Indicates if the function should be run in test version mode or not.
    :param dic_mask_test: The dictionary with the dates and the three generated arrays if the test version is activated.
    :return: Print the message "Dictionary masked of date ... updated" or in case that test version is activated, print
             the message "Both masked dictionaries of date ... updated".
    """

    nrow = dic_values["blue"][date].shape[0]
    ncol = dic_values["blue"][date].shape[1]

    #pbar = tqdm.tqdm(total=total)

    cloud_mask_list = []
    cm_list_test1 = []
    cm_list_test2 = []
    cm_list_test3 = []

    if test_version == 0:

        for r in range(0, nrow):
            for c in range(0, ncol):
                cloud_mask_list.append(mtcd(date, r, c, blue_par, red_blue_par, window_size, cor_coeff, dic_values, dic_mask, 0))
                #pbar.update(1)
        #pbar.close()

        cm_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)

        dic_mask.update({date: cm_array})
        print("Dictionary masked of date %s updated" % (date))

    if test_version == 1:

        for r in range(0,nrow):
            for c in range(0,ncol):
                cm_list_test1.append(mtcd(date, r, c, blue_par, red_blue_par, window_size, cor_coeff, dic_values, dic_mask, 1)[0])
                cm_list_test2.append(mtcd(date, r, c, blue_par, red_blue_par, window_size, cor_coeff, dic_values, dic_mask, 1)[1])
                cm_list_test3.append(mtcd(date, r, c, blue_par, red_blue_par, window_size, cor_coeff, dic_values, dic_mask, 1)[2])
                cloud_mask_list.append(mtcd(date, r, c, blue_par, red_blue_par, window_size, cor_coeff, dic_values, dic_mask, 0))

        cm_array1 = np.asarray(cm_list_test1).reshape(nrow, ncol)
        cm_array2 = np.asarray(cm_list_test2).reshape(nrow, ncol)
        cm_array3 = np.asarray(cm_list_test3).reshape(nrow, ncol)
        cm_array_3d = np.array([cm_array1, cm_array2, cm_array3])
        dic_mask_test.update({date: cm_array_3d})

        cm_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)
        dic_mask.update({date: cm_array})
        print("Both masked dictionaries of date %s updated" % (date))



