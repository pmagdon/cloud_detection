import pandas as pd
from src.first_import import first_import
from src.import_image import import_image, import_cloudfree_reference
from src.timeseries import extract_timeseries
from src.cloud_mask import cloud_mask

#  Run

image_set = []
# empty list to be filled up with the file paths of the images

first_import("data/2015-03-19.tif", image_set)
first_import("data/2015-04-09.tif", image_set)
first_import("data/2015-04-19.tif", image_set)

# imports the file paths to the list. Output: list updated
# to do: import all the images of a folder at one time

dictionary_blue_red = {"blue": {}, "red": {}}
# this empty nested dictionary will be updated with the arrays of numbers which correspond to the pixel reflectance
# values. Form of the dictionary = {"band": {date: image values}}

for images in image_set:
    # reads all the image files in the list
    import_image(images, 3, 1, dictionary_blue_red)

timeseries = extract_timeseries(dictionary_blue_red, "blue", 0, 0)

df = pd.DataFrame(timeseries)  # creates a data frame
df.plot(x="dates", y="values")  # plot time series

dictionary_masked = {}
# empty dictionary which will be updated with the cloud mask of the images indicating the date of the image
# form of the dictionary {date: cloud_mask}

import_cloudfree_reference("data/2015-03-19.tif",dictionary_masked)
# import the first cloud free reference into the dictionary_masked. Since the first image is always cloud free, all
# the import is a matrix of the size of the image filled with True values

for date in [key for key in dictionary_blue_red["blue"]]:
    cloud_mask(date, 3, dictionary_blue_red, dictionary_masked)

