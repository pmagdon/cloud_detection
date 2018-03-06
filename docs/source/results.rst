Results
=======
Date variation of blue parameter was tested and it leads to better results.

In some images, we observed a high variation of the reflectance values, despite their proximity in time and without the
presence of clouds. To take this into account, a variation of the blue test was implemented. The threshold parameter
depends not only on the number of days between the two images, but also on the value of a calculated ratio using the mean
reflection values of the two images. If this ratio is over 1.5 or under 0.5, the value of the blue parameter is
incremented by 1.5. This causes a more selective tagging of cloudy pixels by the blue test, i.e. only pixels where the
refelctance highly variates are identified as clouds.

Variations on blue parameter
----------------------------
The first parameter to adjust is the blue parameter, since the algorithm begins with the blue test identifying possible
cloudy pixels. Plausible values for this parameter are between 2 and 3. In the clip of date 2015-05-15 over a forest
surface, we can observe a cloud:

.. figure::  _static/figures/cloud2015-05-15.PNG
   :width: 45%
   :align:   center

   Cloud on clip of date 2015-05-15.

We run the algorithm over the time series of this forest clip two times: one with the blue parameter set to 2 and the
second time set to 3. The values for the other parameters are set very high, so that they don't reclassify any pixel
tagged as cloud by the blue test to be able to concentrate on the results of changing the blue parameter. A low value of
the blue parameter causes a more sensitive detection of changes in reflection.
This would be positive in the case that the changes in reflection are due to a cloud and negative when they are due to
something else. As we can observe in the next image, the difference in the cloud mask with blue parameter set to 2 (green
cloud mask) and to 3 (red cloud mask)is not very big.

.. figure::  _static/figures/parameter1_2_3.PNG
   :width: 45%
   :align:   center

   Cloud mask over forest cover with blue parameter set to 3 (red) and to 2 (green).
   Image with cloud of date 2015-05-15.

On the other hand, we have the situation in the same time series of not cloudy pixels being flagged as cloud. The image
of 2015-04-09 is cloud free. Still, the blue test identifies some pixels as cloud. The number of not cloudy pixels
identified as cloud is much bigger with the blue parameter set to 2 than to 3.

.. figure::  _static/figures/notcloud_2015-04-15.PNG
   :width: 45%
   :align:   center

   Cloud mask over forest cover with blue parameter set to 3 (red) and to 2 (green).
   Cloud free image of date 2015-04-15.

Therefore, we conclude that while a lower value for the blue band parameter causes a better cloud mask for cloudy pixels,
it also leads to a bigger error of commission. This behaviour was observed not only on forest surface, but also in urban
and agriculture surfaces. The red blue test and, especially, the neighbourhood correlation test amend these wrongly
classified pixels and reclassify them to cloud free in some cases, but not always, like we will see in the next sections.
Taking this into account, we choose the value 3 for the blue parameter.

The reason for this error of commission in the image of the date 2015-04-15 is that the previous image (2015-03-23) has
very low reflectance values in the blue band in the area that is identified as cloud in the next image and therefore,
the blue test identifies a high increase in the blue band reflectance values of this area. The low values in the image
of 2015-03-23 are due to the presence of a cloud. The cloudy pixels in this image have high reflectance values, but the
cloud free pixels have a lower reflectance value than usual for this surface.

.. figure::  _static/figures/2015-03-23.PNG
   :width: 45%
   :align:   center

   Image of date 2015-03-23 partly clouded. Cloud free pixels have very low reflectance values between 5-8%

hacer comentario sobre la forma y mencionar que las dos imagenes pertenecen a la misma time series

.. figure::  _static/figures/2015-04-09.PNG
   :width: 45%
   :align:   center

   Image of date 2015-04-09. The reflectance values are between 9 and 12%.

Variations on red-blue parameter
--------------------------------

Variations on window size parameter
-----------------------------------

Variations on correlation coefficient parameter
-----------------------------------------------
.. figure::  _static/figures/3_1_11_70.jpg
   :width: 45%
   :align:   center

   bangbang


Variations on reference pixels
------------------------------
Test 3 reference images: we take the last 10 images vs we take the last 10 cloud free images. If a shiny object
(like a road) is misclassified as cloud because of a high increase of the reflectance because the reference image had
very low reflectance (sometimes due to clouds that are nearby that maybe don´t let the sunshine reach the earth
surface), this error will happen again and again if we compare only with the cloud free, because it will all the time
compare with the image with the low values. But if we compare with all images, this will not happen.
Road masked as a cloud on a single date instead of a possible long duration (art).
Correlation test enables to reclassify as unclouded images with high reflection, but sometimes reclassifies as unclouded
the thin clouds. More in discussion (buffer) g

Como test 3 no es capaz de quitar todos los pixeles del camino, este se sigue marcando como nube. Como el test 1
compara con el ultimo cloud free, vuelve a dar nube y el test 3 vuelve a quitar parte, pero no todo.
Si el test 2 hubiera reclasificado el camino como no nube, en la imagen siguiente, el test 1 hubierera comparado con la
imagen inmediatamente anterior y no hubiera dado cloud.

Accuracy analysis
------------------
Accuracy matrix for our method and for the delivered product to have a comparison.
Compare our cloud mask with the delivered product

Problems with forest due to fall of leaves.
