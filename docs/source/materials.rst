.. _mat-met:

*********************
Materials and methods
*********************
.. _Data-sets:

Data sets
=========

The data set used in developing the multi-temporal cloud detection algorithm are satellite images taken by the sensor RapidEye.
The characteristics of this satellite are specified in table 1 and the wavelength for each spectral band
can be found on table 2. Several time-series were created for each land cover class and each of these time series contains
12 images from the year 2015. The spectral reflectance pixel values used for the tests are expressed
in percentage. The location of the  images is the
`Hainich-Dün exploratory <http://www.biodiversity-exploratories.de/1/exploratories/>`_, which is situated in the west of Thuringia
close to the border to Hessen.

Hainich-Dün represents one of the three exploratories established in the context of the project biodiversity
exploratories, which studies large-scale and long-term functional biodiversity. The `remote sensing sub-project
<http://www.biodiversity-exploratories.de/1/infrastructure/instrumentation-remote-sensing/>`_ provides area-wide information
on the land cover and the land use of these exploratories. To better understand the relationship between ecosystem functions
and land use intensities, time-series analysis are carried out, which need a previous step of cloud masking.

+--------------------+--------------------+---------------------+------------------------+
|Spatial resolution  |Spectral resolution | Temporal            | Radiometric resolution |
|                    |                    | resolution          |                        |
+====================+====================+=====================+========================+
|    5m              |   0.44 - 0.85      | Daily (off-nadir)/  |         12 bit         |
|                    |                    | 5.5 days (at nadir) |                        |
+--------------------+--------------------+---------------------+------------------------+

 Table 1: Resolutions of the satellite RapidEye.

==========  =====
Type        Wavelength
==========  =====
Blue        440-510
Green       520-590
Red         630-685
Red Edge    690-730
NIR         760-850
==========  =====

Table 2: Spectral bands of the satellite RapidEye.

.. _multi-temporal-cloud-detection:

Multi-temporal cloud detection method
=====================================

In this section, the multi-temporal cloud detection algorithm that we implement is described [HHVD10]_. This algorithm identifies
clouds making use of their high reflection values in the blue spectral band. To decide if a pixel of an image is a cloud
or not, we will make use of a time series, comparing images taken at the same spot with different dates.

We will compare the value of the pixel in the blue band with the value of the same pixel coordinate in the cloud-free pixel
from a previous image. This reference value will allow us to identify a high increase in the pixel reflectance value of
the blue band of the current image, which could be due to the presence of a cloud.
This criterion is expressed in the next formula:::

    pblue(D) - pblue(Dr) > blue_parameter * ( 1 + (D - Dr) / 30 )

Where pblue(D) and pblue(Dr) correspond to the pixel reflectance value in the blue band of the current and of the
reference date. A pixel is tagged as cloudy only if the difference between these two values is above a certain threshold
value: the blue parameter (See `Blue test`_). The value of this parameter varies depending on the
number of days between the two dates. D and Dr are expressed in days and if the images are close in time, the threshold
value tends to be the same value as the blue parameter. In the case that the dates are separated by 30 days, the threshold
parameter value will double. This allows some change in time in the surface reflection.

This comparison of reflectance values in the blue band assumes that the Earth reflection stays stable, which is not
always the case. Changes at the Earth surface like agricultural interventions or natural variations can lead to a sudden
increase of reflectance in the pixels of the affected areas. The first test on the blue band could classify these pixels
as clouds, even if their high reflectance value is not due to the presence of a cloud. To compensate this limitation of
the blue spectral band test, another two tests are run after the first one, whose aim is to assure that the detected
sudden increase of the reflectance value is really due to a cloud.

The first of these two tests compares the increase of reflection in the blue band with the one in the red band (See `Red blue test`_).
If the increase of reflectance in the red band is much greater than the variation in the blue band, it is assumed that the
identified variation in the blue band is not due to a cloud, but has other causes. This causes could be that a field is
cropped or ploughed in agriculture landscapes or that vegetation dries quickly in forest landscapes, which all cause a
high reflection on the red spectral band. The threshold that needs to be exceeded to reclassify the pixel as cloud-free
is specified by the red-blue parameter. This second test can be expressed by the next formula:::

    pred(D) - pred(Dr) > red_parameter * ( pblue(D) - pblue(Dr) )

Where pred(D) and pblue(Dr) correspond to the pixel reflectance value in the red band of the current and of the reference
date.

Another characteristic of clouds is that they don't stay at the same place and with the same shape for a long time. The
reflectance of the pixel neighbourhood of the current image is compared with the reflectance of the same neighbourhood
in one to ten images acquired before the current date (See `Neighbourhood correlation test`_). If the neighbourhood's
reflectances are similar, i.e. if their correlation coefficient is high, can only be due to the absence of a cloud.
The reason for using the pixel reflections from the last ten images as reference and not from the last ten cloud-free
pixels is to prevent that an error of commission remains through the images of the time series. This will be discussed
in more detail in the sub-section :ref:`reference-pixels`.

These two tests are run only on the pixels that are tagged as clouds by the first test using the blue band reflectance
increase criterion. They either assure the positive result and the pixel stays flagged as a cloud or they reclassify the
pixel to cloud free. A pixel that is classified as cloudy by the blue band test is only finally tagged as a cloud if the
other two tests confirm this classification.

The pixel with which we are comparing the current pixel value should be cloud-free because its aim is to be a reference
of a clear-sky reflectance value of the blue band in this specific position of the earth surface. This obliges us to
begin the analysis with a complete cloud-free image, which serves as a reference for the pixels of the first analysed
image. This requirement may be contradictory since the aim of the algorithm is to be able to identify the clouds, but
it needs a cloud-free image to start with the analysis. More about this issue can be read in the :ref:`dicussion` section
of this project, where a solution to this problem is proposed.

A main idea of the time series analysis is that the images are analysed one at a time and at pixel-level. Only when all
pixels of an image are tagged as cloud or cloud-free and this information is saved, the analysis will follow with the
next image. This is because the reference pixel should correspond to the most recent cloud-free pixel before the date of
the current image. If a pixel is tagged as not cloudy, the value of this pixel will be as the reference for the pixel value in
the next image.

Documentation
=============
This algorithm was implemented using Python 3.6 in the IDE Pycharm. The functions were organised in seven different
modules, each one of them storing one to more functions. For the documentation of this project `Sphinx  <http://www.sphinx-doc.org/en/master/>`_
was used. Sphinx is a documentation generator written in Python that uses the markup language reStructuredText and its parsing and
translating suite Docutils to convert the reStructuredText files into HTML websites and other output formats like PDF
(See more under `Sphinx-README <https://github.com/sphinx-doc/sphinx/blob/master/README.rst>`_). The plaintext markup syntax
`reStructuredText <http://docutils.sourceforge.net/rst.html>`_ was chosen among other markup languages for its ease to
read and because it is the default markup language in the Python integrated tools of the IDE Pycharm.

The documentation of the created functions of this cloud detection algorithm was written with help of in-line documentation.
The parameters and the outputs of all functions were declared using docstrings, together with a short and a long description
of what the function executes. This function documentation is presented hereunder along with an explanation of the main
code and the followed steps to create the cloud masks from the raw images.

Implementation of the algorithm
===============================

First import
------------
The very first step is to import the images. For this, we indicate in which path are the images that we want to analyse.
The names of the files found in this path are read and written into a list together with its path.
The first module is called first_import and the only function in this module just writes the file names of the image into a list.

.. automodule:: src.first_import
    :members:

We continue with the creation of an empty nested dictionary. `Dictionaries <https://docs.python.org/2/library/stdtypes.html#typesmapping>`_
are mapping type objects which are able to store values. This values can be indexed by keys. There is also possible to
create one or more dictionaries inside of a dictionary, this is known as a nested dictionary.

The newly created dictionary is called dictionary_blue_red and inside it we find other two dictionaries: the first one
can be accessed by the key "blue" and the second one by the key "red". The dictionary will have then the next structure:
::

    dictionary_blue_red = {"blue": {}, "red": {} }

.. _import-image:

Import image
------------
This dictionary will be filled with arrays representing the images and containing the reflectance values of both the
blue and the red band. For this, the function "import_image" was created, which is stored in the module of the same
name. This module has a second function, the "import_cloud_reference" function. This will be used for importing the first
cloud-free reference image we need to begin the analysis.

.. automodule:: src.import_image
   :members:

Timeseries
----------
Having the reflectance values of the series of images stored in a dictionary makes it possible to create a time series
at pixel level that enables us to visually inspect the variations of the blue band reflectance values over the different
dates. The next function returns a new time series dictionary with the dates and their corresponding values for a given
pixel. We build a plot using this values with help of the library `matplotlib <https://matplotlib.org/index.html>`_.
An example of such a plot will be shown in the results part (see: :ref:`timeseries-plot`).

.. automodule:: src.timeseries
    :members:

Before beginning with the multi-temporal cloud detection analysis, we create two new empty dictionaries that will
store the results of this analysis, i.e. the cloud masks.::

    dictionary_masked = {}
    dictionary_masked_test = {}

The keys will correspond to the date of the image and the values to the cloud masks for each image. A cloud mask for
an image is an array with the size of the image and with one value for each pixel cell. The possible values are:

    * 1 for the pixels that are considered cloud free
    * 0 for pixels tagged as cloud
    * -999 for the case that no data was found at this pixel of the image. Like explained in the description of the
      "`import-image`_" function, pixels of the image with value 0 are imported as no data (np.nan).

The reason to create two dictionaries is that each one of them will store a different output. The dictionary_masked will
store the cloud masks as arrays with the value True if the pixel is cloud free and False if it is cloud and the second
dictionary will store each one of the results of the three tests. This will help the adjustment of the function parameters
for the three tests. How this works is explained in the `Array to raster`_ section.

Search reference
----------------
Like already mentioned, the reference values for the blue and for the red-blue test should correspond to the most
recent cloud free pixel before the date that is currently analysed. A specific function was written to find these
values, which can be found under the "search_reference" module.

.. automodule:: src.search_reference
    :members:

The module "multi_temporal_cloud_detection" is the main analysis module, since here is where we find the functions that
correspond to the `Blue test`_, the `Red blue test`_ and the `Neighbourhood correlation test`_. The `Multi-temporal cloud detection function`_
puts all these tests together and it is the function that determines if a given pixel is
considered cloud or cloud free. In addition, we also find other two functions that the `Neighbourhood correlation test`_
uses: the function`Analysis window`_ that extracts the neighbourhood of a pixel into an array and the function `Correlation array`_
that calculates the correlation coefficient between two arrays.

.. _multi-temp:

Multi-temporal cloud detection
------------------------------
The `Multi-temporal cloud detection function`_ has a parameter named "test_version". If this parameter is set to 0,
the output for a pixel will be
True, False or -999, but if it is set to 1, the function will return three values for each pixel corresponding to each
of the results of the three tests. A detailed explanation of this output can be read in the description of the
`Multi-temporal cloud detection function`_.

.. _blue-test:

Blue test
.........
.. automodule:: src.multi_temporal_cloud_detection
    :members: blue_test

.. _red-blue:

Red blue test
.............
.. automodule:: src.multi_temporal_cloud_detection
    :members: red_blue_test

Analysis window
...............
.. automodule:: src.multi_temporal_cloud_detection
    :members: analysis_window

Correlation array
.................
.. automodule:: src.multi_temporal_cloud_detection
    :members: cor_array

.. _neigh-cor:

Neighbourhood correlation test
..............................
.. automodule:: src.multi_temporal_cloud_detection
    :members: neigh_cor

Multi-temporal cloud detection function
.......................................
.. automodule:: src.multi_temporal_cloud_detection
    :members: mtcd


Cloud mask
..........
The "cloud_mask" function runs the already known `Multi-temporal cloud detection function`_ over all pixels of the image.
Again, we find the "test_version" parameter in this function. If its value is 0, the function will update the "dictionary_masked"
with the cloud masks. If the "test_version" parameter is set to 1, not only the "dictionary_masked" is updated, but also
the "dictionary_masked_test". Three arrays are stored under each date/key of this dictionary, each one of the arrays
corresponding to the result of each test. The goal of creating this dictionary is to export the contained arrays into
multiband raster files with three bands. How these multiband raster files help improve the analysis of the algorithm
is explained in the section `Array to raster`_.

.. automodule:: src.cloud_mask
    :members:

.. _array-to-raster:

Array to raster
...............
The export of the cloud mask arrays into raster files is performed by the two functions in the module array to raster.
The first function creates a raster file of one band with the end result of
the cloud masks and the second one creates a multi band raster file with three bands and each of the bands contains the
results for each of the three tests run in the `Multi-temporal cloud detection function`_.

The mono-band raster files can be opened in a geospatial program, like ArcMap, to display the results. Placing the image under
the cloud mask and setting the pixel value for the pixels tagged as cloud-free to transparent in the symbology options,
allows us to get an idea of the accuracy of the cloud masks, but we can't know which specific result gave each test for
each pixel. Being able to know this information can help us, for example, to understand the reason why a pixel that is a cloud was
tagged as cloud-free by the algorithm. This could be because the blue test didn't identify the cloud or because it did,
but one of the other two tests wrongly reclassified the pixel as cloud free.

Loading the multiband raster files into ArcMap allows us to visualize the results of each test for each pixel. This
increases the understanding of how the algorithm works and which influence each one of the tests has on the final result.
Having this insight also eases the adjustment of the parameters used in the tests and this enables a better analysis and
development of the algorithm.

.. automodule:: src.array_to_raster
    :members:

The adjustment of the parameters was done using clips of the image with the size 500 x 500 m to avoid long processing
time. Three surface classes were identified in the whole image and, for each class, three different clips were created.
Each clip represents a time series. Once the parameters were set, the algorithm was run on bigger images of 2500 x 2500.

Accuracy analysis
=================

To calculate the accuracy of the multi-temporal cloud detection algorithm and determine the error rate and source, some
of the generated cloud masks are used to run a point based accuracy assessment, which is calculated for 3 different
land cover classes: forest, city and field.

For each one of these classes, the cloud masks for the 12 images of the size 2500 x 2500 from the same time series are analysed.
50 points per image are created using the tool `Create accuracy assessment points
<https://desktop.arcgis.com/en/arcmap/latest/tools/spatial-analyst-toolbox/create-accuracy-assessment-points.htm>`_
offered by ArcMap. The sampling strategy is set to "stratified random" to be sure that we get representative points for
cloud and cloud-free areas. This condition causes that the tool sometimes creates more than 50 points, but never less.

There are two types of images that we let out of the accuracy analysis: the first cloud-free image of each time series
and the images with only NA values, since they are ignored by the algorithm. The method used in the accuracy analysis is
the visual assessment. The results of the cloud masks written in the attribute table are compared with the output of the algorithm.
An :ref:`confusion-matrix` is generated with these values and the overall accuracy, the errors of commission and
of omission are calculated for each land cover class.



