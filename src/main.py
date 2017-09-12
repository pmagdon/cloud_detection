import pandas as pd
import numpy as np
from src.first_import import first_import
from src.import_image import import_image
from src.timeseries import extract_timeseries
from src.multi_temporal_cloud_detection import mtcd_test1, mtcd_test2, mtcd_test3

#  Run

image_set = [] # create an empty list

first_import("data/clip1.tif", image_set) # maybe here we can also use a loop and do the first import
                               # for all the images in a folder
first_import("data/clip2.tif", image_set)

dictionary_blue_red = {"blue": {}, "red": {}}

for images in image_set:
    # reads all the image files in the list
    import_image(images, 3, 1, dictionary_blue_red)

# run extract_timeseries function before you continue

timeseries = extract_timeseries(dictionary_blue_red, "blue", 0, 0)

df = pd.DataFrame(timeseries) # creates a dataframe
df.plot(x = "dates", y = "values") # plot time series

# run mtcd function before you continue

output = [] # noch umwandeln in array mit derselben dimension reshape oder so

nrow = next(i.shape[0] for i in dictionary_blue_red["blue"].values())
ncol = next(i.shape[1] for i in dictionary_blue_red["blue"].values())

for row in range(0,nrow):
    for column in range(0,ncol):
        output.append(mtcd_test1(dictionary_blue_red, row , column))

output = [mtcd(dictionary_blue_red, "blue", r, c)
          for r in range(0, nrow)
          for c in range(0, ncol)]

output2 = np.asarray(output).reshape(nrow, ncol)