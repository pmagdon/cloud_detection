Materials and methods
=====================

Since we don´t have any thermal band in our images, we can´t use this method to identify the clouds. We will use another
characteristic of clouds, to wit, their high reflection value in the blue spectral band. To decide if a pixel of an
image is a cloud or not, we will make use of the time series. We will compare its value in the blue band with the value
of the same pixel coordinate in a cloud free pixel from a previous image. This reference value will allow us to
identify a high increase in the blue band reflection pixel value from the current image, which could be due to the
presence of a cloud.
This criterion is expressed in the next formula:
…
Where pblue(D) and pblue(Dr) correspond to the pixel reflectance value of the current and of the reference date. A pixel
is tagged as cloud only if the difference between these two values is above a certain threshold value. This threshold
varies depending on the number of days between the two dates. D and Dr are expressed in days and if the images are
close in time, the threshold value tends to be 0.03. In the case that the dates are separated by 30 days, the
threshold parameter value will double. This allows change in time in the surface reflection. In some images, we
observed a high variation of the reflectance values, despite their proximity in time. To take this into account, the
threshold parameter is also affected by the difference between the mean reflections of the two images. If the ratio
between the two means is above 1.5 or under 0.5, the threshold parameter value is multiplied by 1.5. This increase of
the parameter achieves that only big variations are identified as clouds.
This comparison of reflectance values in the blue band assumes that the earth reflection stays stable, which is not
always the case. Changes at the earth surface like agricultural interventions or natural variations can lead to a sudden
increase of reflectance in the pixels of the affected areas. The first test on the blue band will classify these pixels
as clouds, even if their high reflectance value is not due to the presence of a cloud.
To compensate this limitation of the blue spectral band test, another two tests are run after the first one, whose aim
is to assure that the detected sudden increase of the reflectance value is really due to a cloud.
The first of these two test compares the increase of reflection in the blue band with the one in the red band. If the
increase of reflectance in the red band is much greater than the variation in the blue band, it is assumed that the
identified variation in the blue band is not due to a cloud, but has other causes. This causes could be that a field is
cropped or ploughed in agriculture landscapes or that vegetation dries quickly in forest landscapes, which all cause a
higher reflection on the red spectral band. How much greater the variation of the red band needs to be to reclassify the
pixel as cloud free is specified by the red-blue-threshold parameter.
Another characteristic of clouds is that they don´t stay at the same place and with the same shape for a long time. The
reflectance of the pixel neighbourhood of the current image is compared with the reflectance of the same neighbourhood
in one to ten images acquired before the current date. If the neighbourhood´s reflectances are similar, i.e. if their
correlation coefficient is high, can only be due to the absence of a cloud.
These two tests are only run on the pixels that are tagged as clouds by the first test using the blue band reflectance
increase criterion. They either assure the positive result and the pixel stays flagged as a cloud or they reclassify the
pixel to cloud free. A pixel that is classified as cloud by the blue band test is only finally tagged as cloud if the
other two tests confirm this classification.


The pixel with which we are comparing the current pixel value should be always cloud free, because its aim is to be a
reference of a common value of reflectance of the blue band in this specific position of the earth surface. This obliges
us to begin the analysis with a complete cloud free image, which serves as a reference for the pixels of the first
analysed image. This requirement may be contradictory, since we are developing a code which is able to identify the
clouds, but it needs a cloud free image to start with the analysis. More about this issue can be read in the discussion
part of this project.
A main idea of the time series analysis is that the images are analysed one at a time and at pixel-level. Only when all
pixels of an image are tagged as cloud or cloud free, and this information is saved, the analysis will follow with the
next image. This is because the reference pixel should correspond to the most recent cloud free pixel before the date of
the current image. If a pixel is tagged as cloud free, the value of this pixel will be used for cloud free reference for
the next image.
Problems with forest due to fall of leaves.

.. automodule:: src.first_import
    :members:

.. automodule:: src.import_image
   :members:

.. automodule:: src.timeseries
    :members:

.. automodule:: src.multi_temporal_cloud_detection
    :members:

.. automodule:: src.search_reference
    :members:

.. automodule:: src.cloud_mask
    :members:

.. automodule:: src.array_to_raster
    :members:
