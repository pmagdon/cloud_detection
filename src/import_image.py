import rasterio
import numpy as np


def import_image(file, blue_band, red_band, dic):
    """
    Import the blue and red band pixel values of an image into a dictionary.

    Open the image file, read the values of the selected bands and of the acquisition date and update a nested
    dictionary. Each of the two nested dictionaries corresponds to one band: blue and red.
    The keys of the nested dictionaries will be the dates corresponding to the images and the reflectance values in
    the form of an array will be the values.
    If a value is 0, is replaced with np.nan.


    :param str file: The input file.
    :param int blue_band: The number of the blue band.
    :param int red_band: The number of the red band.
    :param object dic: The image values dictionary.
    :return: Print the message "Dictionary updated".
    """

    im = rasterio.open(file)

    im_blue_band = im.read(blue_band)
    im_red_band = im.read(red_band)

    im_blue_band[im_blue_band == 0] = np.nan
    im_red_band[im_red_band == 0] = np.nan

    date = im.tags()['Acquisition_DateTime'][0:10]

    dic["blue"].update({date: im_blue_band})
    dic["red"].update({date: im_red_band})
    print("Dictionary updated")


def import_cloudfree_reference(file, dic):
    """
    Import the first image of the series which should be a cloud-free reference.

    Open the first cloud-free image which serves as a reference. Open the file and read a band. Read the date of
    acquisition. Create an array full of "True" values with the shape of the image array. Update the masked dictionary
    with the created array and its correspondent date of acquisition.

    :param str file: The input file.
    :param object dic: The masked dictionary.
    :return: Print the message "First cloud free reference imported to dictionary".
    """
    first_ref_values = rasterio.open(file).read(1)
    date_first_ref = rasterio.open(file).tags()['Acquisition_DateTime'][0:10]
    first_ref_mask = np.full_like(first_ref_values, True, dtype= bool)
    dic.update({date_first_ref: first_ref_mask})
    print("First cloud free reference imported to dictionary")



