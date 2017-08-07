import rasterio
from dateutil.parser import parse
import matplotlib.pyplot as plt
import numpy as np

# Test
# im1 = rasterio.open('clip1.tif') # imports image
# im1b1 = im1.read(1) # reads band 1
# date1 = im1.tags()['Acquisition_DateTime'] # reads date of the image
# im2 = rasterio.open('clip2.tif')
# im2b1 = im2.read(1)
# date2 = im2.tags() ['Acquisition_DateTime']
# print(type(im1.tags()['Acquisition_DateTime'])) # gives class of date

# date1 = parse(date1) # converts class string to datetime
# date2 = parse(date2)
# print(type(date1))

# dict = {'2015/5/10': im1b1, '2015/5/15' : im2b1}

def import_image(file, band, dict):
    # "Reads the image file, takes the values of the selected band
    # and of the acquisition time and updates a dictionary with them"
    im = rasterio.open(file)
    imb = im.read(band)
    date = im.tags()['Acquisition_DateTime']
    dict.update({date: imb})
    print("Dictionary updated")
    return 1

dictionary = {}
tmp1 = import_image('clip1.tif',1,dictionary)
tmp2 = import_image('clip2.tif',1,dictionary)

im1b1 = im1b1[:,:,np.newaxis] # adding a new dimension
im2b1 = im2b1[:,:,np.newaxis]

array3d = np.concatenate((im1b1, im2b1), axis = 2)  # concatenates the arrays by their 3rd dimension

values = array3d[0,0,:] # extracts from all images the pixel values in the position row = 1, column = 1

plt.plot(tuple([date1,date2]), ([array3d[0,0,:]]),'o')

x1 = im1b1[0, 0] # subset first pixel of the image 1
x2 = im2b1[0, 0]# subset first pixel of the image 2
plt.plot([date1, date2], [x1, x2])  # plot time series


[date1,date2]