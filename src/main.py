import pandas as pd
import os
from src.first_import import first_import
from src.import_image import import_image, import_cloudfree_reference
from src.timeseries import extract_timeseries
from src.cloud_mask import cloud_mask
from src.array_to_raster import array2raster

#  Run

image_set = []
# empty list to be filled up with the file paths of the images

files = os.listdir("C:/Users/anpla/PycharmProjects/cloud_detection/data")
# reads the names of the files in the given directory into a list

for file in files:
    # for loop to import all the file paths of the files in the folder data into the list image_set.
    # Output: list updated
    first_import("data/" + file, image_set)

dictionary_blue_red = {"blue": {}, "red": {}}
# this empty nested dictionary will be updated with the arrays of numbers which correspond to the pixel reflectance
# values. Form of the dictionary = {"band": {date: image values}}

for images in image_set:
    # reads all the image files in the list
    import_image(images, 1, 3, dictionary_blue_red)

#timeseries = extract_timeseries(dictionary_blue_red, "blue", 0, 0)

#df = pd.DataFrame(timeseries)  # creates a data frame
#df.plot(x="dates", y="values")  # plot time series

dictionary_masked = {}
# empty dictionary which will be updated with the cloud mask of the images indicating the date of the image
# form of the dictionary {date: cloud_mask}

import_cloudfree_reference("data/2015-03-19.tif",dictionary_masked)
# import the first cloud free reference into the dictionary_masked. Since the first image is always cloud free, all
# the import is a matrix of the size of the image filled with True values

#for date in [key for key in dictionary_blue_red["blue"]]:
#    cloud_mask(date, 5, dictionary_blue_red, dictionary_masked)

cloud_mask("2015-07-04",1.5, 1.5, 13, 0.55, dictionary_blue_red, dictionary_masked)


array2raster("data/2015-05-15.tif", 'cm_2015-05-15.tiff', 5, 5, dictionary_masked, "2015-05-15")

