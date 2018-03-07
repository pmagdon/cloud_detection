Results
=======

Variations on blue parameter
----------------------------
The first parameter to adjust is the blue parameter, since the algorithm begins with the blue test identifying possible
cloudy pixels. Plausible values for this parameter are between 2 and 3. In the clip of date 2015-05-15 over a forest
surface, we can observe a cloud:

.. figure::  _static/figures/par1_fig1_forest1.PNG
   :width: 45%
   :align:   center

   Figure 1: Cloud on clip of date 2015-05-15.

We run the algorithm over the time series of this forest clip two times: one with the blue parameter set to 2 and the
second time set to 3. The values for the other parameters are set very high, so that they don't reclassify any pixel
tagged as cloud by the blue test to be able to concentrate on the results of changing the blue parameter. A low value of
the blue parameter causes a more sensitive detection of changes in reflection.
This would be positive in the case that the changes in reflection are due to a cloud and negative when they are due to
something else. In the next figure we can observe two cloud masks overlapping. The cloud masks with the blue parameter
set to 3 is represented in red. The green cloud mask is created with the blue parameter set to 2 and it covers the area
of the red cloud mask and a bit more, but we can notice that this difference between both masks is small.

.. figure::  _static/figures/par1_fig2_forest1.PNG
   :width: 45%
   :align:   center

   Figure 2: Cloud mask over forest cover with blue parameter set to 3 (red) and to 2 (green).
   Image with cloud of date 2015-05-15.

On the other hand, we have the situation in the same time series of not cloudy pixels being flagged as cloud. The image
of 2015-04-09 is cloud free. Still, the blue test identifies some pixels as cloud. Again, we show both cloud masks
overlapping to be able to see the difference between them. The number of not cloudy pixels wrongly identified as cloud
is much bigger with the blue parameter set to 2 (green cloud mask) than to 3 (red cloud mask).

.. figure::  _static/figures/par1_fig3_forest1.PNG
   :width: 45%
   :align:   center

   Figure 3: Cloud mask over forest cover with blue parameter set to 3 (red) and to 2 (green).
   Cloud free image of date 2015-04-15.

Therefore, we conclude that while a lower value for the blue band parameter causes a slightly better cloud mask for
cloudy pixels, it also leads to a bigger error of commission. This behaviour was observed not only on forest surface,
but also in urban and agriculture surfaces. The red blue test and, especially, the neighbourhood correlation test amend
these wrongly classified pixels and reclassify them to cloud free in some cases, but not always, like we will see in the
next sections. Taking this into account, we decide that the value 3 is convenient for the blue parameter.

Like already explained in the section materials and methods, the value of the blue parameter variates depending on the
the time passed between the dates of the two pixels being compared. If the two pixels are far away in time, the parameter
is increased. This temporal dependence of the blue parameter was also tested by letting it out in some runs of the algorithm.
All results showed a better cloud mask for the case of date depending variation of the blue parameter.

In some images, we observed a high variation of the reflectance values, despite their proximity in time and without the
presence of clouds. To take this into account, a variation of the blue test was implemented. The threshold parameter
depends not only on the number of days between the two images, but also on the value of a calculated ratio using the mean
reflection values of the two images. If this ratio is over 1.5 or under 0.5, the value of the blue parameter is
incremented by 1.5. This causes a more selective tagging of cloudy pixels by the blue test, i.e. only pixels where the
refelctance highly variates are identified as clouds.


Impact of clouds on nearby pixels
---------------------------------
The reason for the error of commission in the image shown on figure 3 are the very low reflectance values in the blue band
of the previous image of the same time series with date 2015-03-23 in the area that is cloud free (see figure 4).
This causes that the blue test identifies a high increase in the blue band reflectance values of this
area. The low values in the image of 2015-03-23 are due to the presence of a cloud. The cloudy pixels in this image have
high reflectance values, but the cloud free pixels have a lower reflectance value than usual for this surface. We can
recognise that the shape of the cloud mask in figure 3 corresponds to the part of the image in figure 4 that is cloud free.

.. figure::  _static/figures/imp_fig4_forest1.PNG
   :width: 45%
   :align:   center

   Figure 4: Image of date 2015-03-23 partly clouded. Cloud free pixels have very low reflectance values between 5-8%


.. figure::  _static/figures/imp_fig5_forest1.PNG
   :width: 45%
   :align:   center

   Figure 5: Image of date 2015-04-09. The reflectance values are between 9 and 12%.


Variations on red-blue parameter
--------------------------------
The red-blue test should be able to reclassify wrongly cloud-tagged pixels by the blue test, which are really cloud free.
This reclassification should occur especially in agricultural or forest landcovers where the cropping or the drying of the
vegetation theoretically provokes a higher reflection on the red band than in the blue band. By running the algorithm
with different values for the red blue parameter, we conclude that possible values for this test are between 1 and 2.
With higher values, the test doesn't reclassify any pixels.

In the next figure we can observe the changes in reflection between two images of the same time series. This changes
are due to agricultural interventions.

.. figure::  _static/figures/par2_fig1_field2.PNG
   :width: 80%
   :align:   center

   Figure 6: Left image of date 2015-07-04, right image of date 2015-08-08.

With the blue parameter set to 2, the blue test wrongly identifies many pixels of the left field as clouds. The red blue
test is able to amend this error by reclassifying a great part of this pixels with the red blue parameter set to 2. See
next figure:

.. figure::  _static/figures/par2_fig2_field2_cm.PNG
   :width: 45%
   :align:   center

   Figure 7: Cloud mask for image of date 2015-08-08. Yellow pixels were first classified as clouds by the blue test, but
   then the red-blue test reclassifies them as cloud free.

The disadvantage of the red blue test is that with the parameter set to 2 it not always succeeds in reclassifying the
cloud free pixels like in the previous figure, but it always reclassifies the thin clouds. This can be observed in
figure 9, where yellow pixels located at the edges of the cloud represent reclassified pixels by the red blue test.


.. figure::  _static/figures/par2_fig3_field2.PNG
   :width: 45%
   :align:   center

   Figure 8: Image with cloud of date 2015-05-15.


.. figure::  _static/figures/par2_fig4_field2_cm.PNG
   :width: 45%
   :align:   center

   Figure 9: Cloud mask of date 2015-05-15. Red pixels are classified as cloudy by the blue test and not reclassified
   by the other two tests. Yellow pixels are reclassified by the red blue test, pink pixels are reclassified by the
   neighbourhood correlation test and white pixels are reclassified by both tests. The red pixels correspond to the final
   cloud mask.

If we reduce the parameter to 1.5 or even to 1, the reclassifying of erroneously classified pixels works better, but
still not as good as expected, but a very great part of the pixels that are really clouds are also reclassified, which
leads to a great error of omission. Therefore, the red blue parameter is set to 2 and it is pointed out that its influence
on the end cloud mask is minor in comparision with the impact of the neighbourhood correlation, as we will see in the
next section.


Variations on correlation coefficient parameter
-----------------------------------------------

The neighbourhood correlation test reclassifies a pixel if its neighbourhood highly correlates with the same
neighbourhoods of any of the ten previous images. The correlation coefficient parameter indicates above which correlation
a pixel will be reclassified. Therefore, if the parameter is high, less pixels will be reclassified than if the parameter
is low. The next image shows an urban landcover with some bright objects like buildings and roads that are classified as
clouds by the blue test.

.. figure::  _static/figures/cc_fig1_city.PNG
   :width: 45%
   :align:   center

   Figure 10: Image of date 2015-04-19.

We run the algorithm using two different values for the correlation coefficient parameter: 85% and 55%. All the pixels
coloured in red or pink are classified as cloud by the blue test, but the pink ones are again reclassified as cloud free
by the neighbourhood correlation test. In figure 11 we can recognise that with a low parameter value more pixels are
reclassified. The reason why not all the pixels are reclassified in the right image despite the low parameter value is
that this is only the third image in the time series, which implies that the comparision can be only done with the two
previous neighbourhoods, which both have low values of reflectance.

.. figure::  _static/figures/cc_fig2_city.PNG
   :width: 80%
   :align:   center

   Figure 11: Cloud masks generated with a correlation coefficient parameter of 85% (left) and 55% (right). Pink pixels
   are reclassified as cloud free by the neighbourhood correlation test.

Like in the red blue test, we have the inconvenient that a low parameter value that achieves a very good reclassification
of pixels that are cloud free, will also reclassify some cloudy pixels of thin clouds. This behaviour can be noticed in
figure 13, where a high parameter value avoids the wrongly reclassification of any of the cloudy pixels as cloud free, while
with a low parameter value, some of these pixels are reclassified. We can also recognise again the behaviour of the red
blue test by looking at the yellow pixels. Some of the pixels are reclassified by this tests, which red blue parameter was
set to 2 in this run.

.. figure::  _static/figures/cc_fig3_city.PNG
   :width: 45%
   :align:   center

   Figure 12: Image of date 2015-05-15 with cloud.

.. figure::  _static/figures/cc_fig4_city.PNG
   :width: 80%
   :align:   center

   Figure 13: Cloud masks generated with a correlation coefficient parameter of 85% (left) and 55% (right).

Again, we have to find a compromise between a good reclassification of cloud free pixels and a not very high amount of
cloudy pixels being reclassified as cloud free. After running the algorithm with different values for this parameter in
different time series and landcovers, we decide to set the correlation coefficient parameter to 70%.

Variations on window size parameter
-----------------------------------

Another possible variation of the neighbourhood correlation test is the window size for this neighbourhood. It was noticed
that the increase of this parameter highly increased the running time of the algorithm.


.. figure::  _static/figures/ws_fig3_field1.PNG
   :width: 45%
   :align:   center

.. figure::  _static/figures/ws_fig1_field1.PNG
   :width: 80%
   :align:   center

.. figure::  _static/figures/ws_fig2_field1.PNG
   :width: 80%
   :align:   center


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
-----------------
Accuracy matrix for our method and for the delivered product to have a comparison.
Compare our cloud mask with the delivered product

Problems with forest due to fall of leaves.
