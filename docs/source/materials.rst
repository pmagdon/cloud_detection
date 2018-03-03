Materials and methods
=====================

Cloud detection using time series
---------------------------------
Since we don´t have any thermal band in our images, we can´t use this method to identify the clouds. We will use another
characteristic of clouds, to wit, their high reflection value in the blue spectral band. To decide if a pixel of an
image is a cloud or not, we will make use of a time series, comparing images taken at the same spot with different dates.
We will compare the value of the pixel in the blue band with the value of the same pixel coordinate in a cloud free
pixel from a previous image. This reference value will allow us to identify a high increase in the pixel reflectance value
of the blue band of the current image, which could be due to the presence of a cloud.
This criterion is expressed in the next formula:
…
Where pblue(D) and pblue(Dr) correspond to the pixel reflectance value of the current and of the reference date. A pixel
is tagged as cloud only if the difference between these two values is above a certain threshold value. This threshold
varies depending on the number of days between the two dates. D and Dr are expressed in days and if the images are
close in time, the threshold value tends to be 0.03. In the case that the dates are separated by 30 days, the
threshold parameter value will double. This allows change in time in the surface reflection.

This comparison of reflectance values in the blue band assumes that the earth reflection stays stable, which is not
always the case. Changes at the earth surface like agricultural interventions or natural variations can lead to a sudden
increase of reflectance in the pixels of the affected areas. The first test on the blue band could classify these pixels
as clouds, even if their high reflectance value is not due to the presence of a cloud.
To compensate this limitation of the blue spectral band test, another two tests are run after the first one, whose aim
is to assure that the detected sudden increase of the reflectance value is really due to a cloud.

The first of these two test compares the increase of reflection in the blue band with the one in the red band. If the
increase of reflectance in the red band is much greater than the variation in the blue band, it is assumed that the
identified variation in the blue band is not due to a cloud, but has other causes. This causes could be that a field is
cropped or ploughed in agriculture landscapes or that vegetation dries quickly in forest landscapes, which all cause a
high reflection on the red spectral band. How much greater needs to be the variation in the red band than in the blue
band to reclassify the pixel as cloud free is specified by the red-blue-threshold parameter. This second test can be
expressed in the next formula:

Another characteristic of clouds is that they don´t stay at the same place and with the same shape for a long time. The
reflectance of the pixel neighbourhood of the current image is compared with the reflectance of the same neighbourhood
in one to ten images acquired before the current date. If the neighbourhood's reflectances are similar, i.e. if their
correlation coefficient is high, can only be due to the absence of a cloud. The reason for using the pixel reflections
from the last ten images as reference and not from the last ten cloud free pixels is to prevent that an error of
commission remains through the images of the time series. This will be explained with more detail in the results part.

These two tests are run only on the pixels that are tagged as clouds by the first test using the blue band reflectance
increase criterion. They either assure the positive result and the pixel stays flagged as a cloud or they reclassify the
pixel to cloud free. A pixel that is classified as cloud by the blue band test is only finally tagged as cloud if the
other two tests confirm this classification.

The pixel with which we are comparing the current pixel value should be cloud free, because its aim is to be a reference
of a cloud free reflectance value of the blue band in this specific position of the earth surface. This obliges us to
begin the analysis with a complete cloud free image, which serves as a reference for the pixels of the first analysed
image. This requirement may be contradictory, since the aim of the algorithm is to be able to identify the clouds, but
it needs a cloud free image to start with the analysis. More about this issue can be read in the discussion part of this
project, where a solution to this problem is proposed.

A main idea of the time series analysis is that the images are analysed one at a time and at pixel-level. Only when all
pixels of an image are tagged as cloud or cloud free, and this information is saved, the analysis will follow with the
next image. This is because the reference pixel should correspond to the most recent cloud free pixel before the date of
the current image. If a pixel is tagged as cloud free, the value of this pixel will be used for cloud free reference for
the next image.

Documentation
-------------
This algorithm was implemented using Python 3.6 in the IDE Pycharm. The functions were organised in seven different
modules, each one of them storing one to more functions. For the documentation of this project Sphinx was used. Sphinx
is a documentation generator written in Python that uses the markup language reStructuredText and its parsing and
translating suite Docutils to convert the reStructuredText files into HTML websites and other output formats like PDF.
Source: https://github.com/sphinx-doc/sphinx/blob/master/README.rst

The plaintext markup syntax reStructuredText was chosen among other markup languages for its ease to read and because
it is the default markup language in the Python integrated tools of the IDE Pycharm.
Source: http://docutils.sourceforge.net/rst.html
The documentation of the created functions of this cloud detection algorithm was created with help of in-line
documentation. The parameters and the outputs of all functions were declared using docstrings, together with a short
and a long description of what the function executes. This function documentation is presented hereunder along with
an explanation of the main code and the followed steps to create the cloud masks from the raw images.

The very first step is to import the images. For this, we indicate in which path are the images that we want to analyse.
The names of the files found in this path are read and written into a list together with its path.
The first module is called first_import and the only function in this module of the same name as the module just writes
the file names of the image into a list.

.. automodule:: src.first_import
    :members:

We continue with the creation of an empty nested dictionary. Dictionaries are mapping type object which are able to store
values. This values can be indexed by keys. Source: https://docs.python.org/2/library/stdtypes.html#typesmapping
There is also possible to create one or more dictionaries inside of a dictionary, this are known as nested dictionaries.
The new created dictionary is called dictionary_blue_red and inside it we find other two dictionaries: the first one
can be accessed by the key "blue" and the second one by the key "red". The dictionary will have then the next structure:
::

    dictionary_blue_red = {"blue": {}, "red": {} }

This dictionary will be filled with arrays representing the images and containing the reflectance values of both the
blue and the red band. For this, the function import_image() was created, which is stored under the module of the same
name. This module has a second function, the import_cloud_reference() function. This will be used for the case that we
need a completely cloud free reference image to begin the analysis, like was explained above these lines.

.. automodule:: src.import_image
   :members:

Having the reflectance values of the series of images stored in a dictionary makes it possible to create a time series
at pixel level that enables us to visually inspect the variations of the blue band reflectance values over the different
dates. The next function returns a new time series dictionary with the dates and their corresponding values for a given
pixel. The time series dictionary is converted into a data frame with help of the pandas library, a library providing
data structures and data analysis tools for Python. Source: https://pandas.pydata.org/
The data frame structure is more convenient for the creation of a plot. An example of such a plot will be shown in the
results part.

.. automodule:: src.timeseries
    :members:

Before beginning with the multi temporal cloud detection analysis, we create two new empty dictionaries that will
store the results of this analysis, i.e. the cloud masks.::

    dictionary_masked = {}
    dictionary_masked_test = {}

The keys will correspond to the date of the image and the values to the cloud masks for each image. A cloud mask for
an image is an array with the size of the image and with one value for each pixel cell. The possible values are:

    * 1 for the pixels that are considered cloud free
    * 0 for pixels tagged as cloud
    * -999 for the case that no data was found at this pixel of the image. Like explained in the description of the
      import_image() function, pixels of the image with value 0 are imported as no data (np.nan).

The reason to create two dictionaries is that each onr of them will store a different output. The dictionary_masked will
store the cloud masks as arrays with the value True if the pixel is cloud free and False if it is cloud  and the second
dictionary will store each one of the results of the three tests. This will help the task of adjusting the parameters of
the functions containing the three tests. How this works is explained in the description of the the cloud mask module.

blablablabla reference values
.. automodule:: src.search_reference
    :members:

The module multi_temporal_cloud_detection is the main analysis module, since here is where we find the functions that
corresponds to the blue test, the red-blue test and the neighbourhood correlation test. The mtcd() function, which is
also defined under this module, puts all these tests together and it is the function that determines if a given pixel is
considered cloud or cloud free. In addition, we also find other two functions that the neighbourhood correlation test
uses, the analysis_window() function that extracts the neighbourhood of a pixel into an array and the cor_test3()
function that calculates the correlation coefficient between two arrays.

The mtcd() function has a parameter named test_version. If this parameter is set to 0, the output for a pixel will be
True, False or -999, but if it is set to 1, the function will return three values for each pixel corresponding to each
of the results of the three tests. A detailed explanation about this output can be read in the description of the mtcd()
function.

.. automodule:: src.multi_temporal_cloud_detection
    :members: mtcd_test1, mtcd_test2, analysis_window, cor_test3, mtcd_test3, mtcd

The cloud_mask() function which is stored in the cloud mask module runs the already known multi temporal cloud detection
function over all pixels of the image. Again, we have the test version parameter. If the value of this is 0, the function
will update the dictionary_masked with the cloud masks. If the test version parameter is set to 1, not only the
dictionary_masked is updated, but also the dictionary_masked_test. Three arrays are stored under each date/key of this
dictionary, each one of the arrays corresponding to the result of each test. The goal of creating this dictionary is to
export the contained arrays into multi band rasters with three bands, each one of them corresponding to each array. This
raster file can be open in a geospatial program, like ArcMap, which allows to easily visualize the results of each test
for each pixel. This increases the understanding of how the algorithm works and which influence each of the tests has.
Having this insight eases the adjustment of the parameters used in the tests and enables an easier analysis and
development of the algorithm.


.. automodule:: src.cloud_mask
    :members:

bangbangbang

.. automodule:: src.array_to_raster
    :members:

enlazar con la forma de decidir los parametros.