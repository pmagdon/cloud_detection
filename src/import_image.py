import rasterio


def import_image(file, band, dic):
    # "Reads the image file, takes the values of the selected band
    # and of the acquisition time and updates a dictionary with them"
    im = rasterio.open(file)
    imb = im.read(band)
    date = im.tags()['Acquisition_DateTime'][0:10]
    dic.update({date: imb})
    print("Dictionary updated")

dictionary = {}

import_image('clip1.tif', 1, dictionary)
import_image('clip2.tif', 1, dictionary)
