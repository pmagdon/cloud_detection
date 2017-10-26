import pandas as pd
from src.first_import import first_import
from src.import_image import import_image
from src.timeseries import extract_timeseries
from src.cloud_mask import cloud_mask

#  Run

image_set = []
# empty list to be filled up with the file paths of the images

first_import("data/clip1.tif", image_set)
first_import("data/clip2.tif", image_set)
# imports the file paths to the list. Output: list updated
# to do: import all the images of a folder at one time

dictionary_blue_red = {"blue": {}, "red": {}}
# this empty nested dictionary will be updated with the arrays of numbers which correspond to the pixel reflectance
# values. Form of the dictionary = {"band": {date: image values}}

for images in image_set:
    # reads all the image files in the list
    import_image(images, 3, 1, dictionary_blue_red)

# run extract_timeseries function before you continue

timeseries = extract_timeseries(dictionary_blue_red, "blue", 0, 0)

df = pd.DataFrame(timeseries)  # creates a dataframe
df.plot(x="dates", y="values")  # plot time series

# run mtcd function before you continue

cloud_mask_dictionary = {}
# empty dictionary which will be updated with the cloud mask of the images indicating the date of the image
# form of the dictionary {date: cloud_mask}

cloud_mask(dictionary_blue_red, date, cloud_mask_dictionary)
# creates a cloud mask for a given date with help of mtcd() function
# updates the cloud mask dictionary with the cloud mask of a given date

# Next: test 1 and test 2 need a free cloud pixel as reference which should be so recent in time as possible
# Search free cloud pixel for reference in cloud_mask_dictionary beginning with most recent date: cloud free pixels
# in cloud_mask_dictionary are tagged as True
# When you find it: remember the date
# Search this date in the blue_red_dictionary and take the pixel value of it:
# you have your free cloud reference pixel value



