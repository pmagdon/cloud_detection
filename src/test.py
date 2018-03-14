import numpy as np

######## Search function example ###########

test_dic = {"date0": np.matrix([[0,0],[np.nan, np.nan]]), "date1": np.full((3, 3), 1, int),
            "date2":  np.full((3, 3), np.nan), "date3": np.full((3,3), 3, int), "date4": np.matrix([[np.nan,2],[3,4]])}

#for date in dictionary_blue_red["blue"].keys():
#    print(date + str(": ") + str(np.mean(dictionary_blue_red["blue"][date])))

#### list search reference function ####

# cloud_mask("2015-05-15", 1.5, 1.5, 13, 0.55, dictionary_blue_red, dictionary_masked)
# array2raster("data/2015-03-19.tif", 'cm_2015-03-19.tiff', 5, 5, dictionary_masked, "2015-03-19")

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

    value_pixel = [value[row,col] for key, value in dic_values[band_name].items() if key in key_images]
    mask_pixel = [value[row,col] for key, value in dic_mask.items() if key in key_images]

    #mask_pixel = [value[row, col] for value in mask_images]
    #value_pixel = [value[row, col] for value in value_images]

    indices_not_cloud = [index for index, value in enumerate(mask_pixel) if value == 1][-10:0]

    date_cloudfree = [key_images[i] for i in indices_not_cloud]
    values_cloudfree = [value_pixel[i] for i in indices_not_cloud]

    return date_cloudfree, values_cloudfree


###################################################

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [9.5, 6.3, 10.9, 12.3, 12.9, 8.6, 0, 42.3, 3.3, 6.2, 0, 9.7]
labels = ['03-19', '03-23', '04-09', '04-15', "04-19", "04-24", '05-10','05-15',
          '07-04', '08-08', '08-23', '10-02']



fig = plt.figure()

ax = fig.add_subplot(111)

plt.plot(x, y,  marker='o', )
# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation='vertical')
plt.tick_params(labelsize=16)

# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)

plt.ylabel('reflectance values [%]', fontsize = 20)

ax.annotate(" ", xy=(8, 42.3), xytext=(9, 40), arrowprops=dict(facecolor='black', shrink=0.01))
