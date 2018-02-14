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

files = os.listdir("C:/Users/aplazas/PycharmProjects/cloud_detection/data/hainich_clouds/field")
# reads the names of the files in the given directory into a list

for file in files:
    # for loop to import all the file paths of the files in the folder data into the list image_set.
    # Output: list updated
    first_import("data/hainich_clouds/field/" + file , image_set)

dictionary_blue_red = {"blue": {}, "red": {}}
# this empty nested dictionary will be updated with the arrays of numbers which correspond to the pixel reflectance
# values. Form of the dictionary = {"band": {date: image values}}

for images in image_set:
    # reads all the image files in the list
    import_image(images, 1, 3, dictionary_blue_red)

timeseries = extract_timeseries(dictionary_blue_red, "blue", 56, 85)

#df = pd.DataFrame(timeseries)  # creates a data frame
#df.plot(x="dates", y="values")  # plot time series

dictionary_masked = {}
# empty dictionary which will be updated with the cloud mask of the images indicating the date of the image
# form of the dictionary {date: cloud_mask}

import_cloudfree_reference("data/hainich_clouds/field/2015-03-19T110911_RE3_1B-NAC_20835988_303428_ortho_sr_clip_25km_field.tif", dictionary_masked)
# import the first cloud free reference into the dictionary_masked. Since the first image is always cloud free, all
# the import is a matrix of the size of the image filled with True values

for date in list(dictionary_blue_red["blue"].keys())[1:]:
    cloud_mask(date, 3, 150, 7, 0.75, dictionary_blue_red, dictionary_masked, 0)

for mask in dictionary_masked:
    array2raster("data/"+mask+".tif", "test3_55_"+mask+".tiff", 5, 5, dictionary_masked, mask)

# cloud_mask("2015-05-15", 1.5, 1.5, 13, 0.55, dictionary_blue_red, dictionary_masked)
# array2raster("data/2015-03-19.tif", 'cm_2015-03-19.tiff', 5, 5, dictionary_masked, "2015-03-19")

