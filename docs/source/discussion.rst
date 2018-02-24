Discussion
==========
The first image of the time series, which is also the most distant in time, needs to be completely cloud free. This
requirement is not convenient, since the aim of the algorithm is to be able to detect clouds in the images. A solution:
first cloud free reference: obtained by a simple threshold on the blue band reflectance, mosaic with pixels that are
cloud free according to this simple threshold test. (Backward processing WTF)

Very slow, code more efficient. Not two different dictionaries (values and mask), but the image always together with
its mask

Test 3 correlation coefficient parameter: if low value a lot of pixels are reclassified and if the classification was
wrong this is a good thing, but if the classification was right this leads to wrong reclassifications. Something in the
middle.

Dificultades debidas a la heterogeneidad de las nubes (finas gruesas definidas no)
Sombras?
Bordes nubes
Paisaje distinto -> parametros siguen sirviendo?