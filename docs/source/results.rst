Results
=======

In some images, we observed a high variation of the reflectance values, despite their proximity in time and without the
presence of clouds. To take this into account, the threshold parameter is not only influenced by the number of days
between the two images, but also by the calculated ratio between the mean reflections of the two images.
If this ratio is above 1.5 or under 0.5, the threshold parameter value is multiplied by 1.5. This increase of
the parameter achieves that only big variations are identified as clouds.

Variations on blue parameter
----------------------------

Parameter 1 value 3. Lower: too many pixels identified as cloud. Error of commission is big.
Date variation of parameter 1 is better.
Mean variation changing parameter 1 leads to better results.

Variations on red-blue parameter
--------------------------------

Variations on window size parameter
-----------------------------------

Variations on correlation coefficient parameter
-----------------------------------------------



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
