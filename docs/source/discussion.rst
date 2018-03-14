.. _dicussion:

**********
Discussion
**********

Despite the relatively high value of the calculated overall accuracy (See :ref:`confusion-matrix`), we have to look at
these results with a critical eye. First, for time reasons, only one time series per land cover class was analysed and a
limited number of assessment points was created. The amount of images with clouds in each time series varies between 2 and
3, which is not a large number for calculating the accuracy of their cloud masks. Second, although image clips from three
different land cover classes were selected to assure the representation of the heterogeneity of the landscape, their area
is limited to 2500 x 2500 due to long execution time needed to run this algorithm. The visual inspection of the resulting
cloud masks allows us to recognize room for improvement.

The difficulties in cloud recognition with the threshold approach are due to the high spectral variability of clouds and of
land cover [BrWZ15]_. Clouds are not the only targets with high reflectance values in the visible bands and some clouds are not
completely opaque and present reflectance values that depend on the Earth surface features below them. This makes the setting
of a threshold parameter for detecting clouds a challenging task [HeCy09]_. We were confronted with this difficulty when setting
the values for all four parameters: blue, red blue, window size and correlation coefficient parameter. For all of them, we
had to find a compromise between a high error of commission and a high error of omission (see :ref:`results`). This challenge is also
described by [HHVD10]_ for the case of the neighbourhood correlation test in a very similar way to our results: the
correlation test enables the reclassification of not cloudy pixels, but also sometimes reclassifies as unclouded the pixels
with very thin clouds.

It was observed that this issue was especially problematic in the case of the red-blue test, which also had a minor influence
in the reclassifying of not cloudy pixels compared to the neighbourhood correlation test (see :ref: `variations-red`).
It should be considered to remove this test from the algorithm and to build a new one which fulfils its assigned task: the
reclassification of pixels in cases where the bright reflectance increase is caused by a rapid drying of the vegetation
or cropping of agricultural landscapes (see: :ref:´multi-temporal-cloud-detection´). By the observation that the red-blue
test manages to reclassify the pixels of some fields, but not of other, we conclude that this test is not adequate for
all type of agricultural changes that we should consider. Figure 3 of the article [HHVD10]_ shows a higher increase of the red band
reflectance values in comparison with the values of the blue band when a field is cropped or ploughed. As this is not
the observed behaviour in our images, we should consider selecting some pixels that the blue test wrongly classifies as
clouds due to agriculture interventions or natural events and create a similar time series plot as the latter mentioned,
where we could observe the changing of the values in the different reflectance bands. In this way, we could maybe recognise
some pattern and decide which band or band combination is adequate to create a test that manages to reclassify these
pixels as cloud free.

Regarding the blue test and the neighbourhood correlation test, we can conclude that they provide satisfying results in
general. Still, there are some possible modifications that could improve their accuracy. Both tests use the reflectance
values of the blue band. This band was selected because the surface reflectance of a land pixel tends to change slowly
in time, especially at short wavelengths (400-500 nm), that correspond to the blue band. Therefore, this would be the best
wavelength to identify a sudden increase of reflectance due to the presence of a cloud [HHVD10]_. Nevertheless, other methods
use the difference between the green and the red band for cloud detection [BrWZ15]_. To decide which band adjusts better to the
characteristics of our images, we should proceed again with the creation of a time series plot, in this case,  where we
can see the modifications of the cloudy pixel reflectance values for all the bands of the RapidEye satellite.

The blue test bases in the comparison of the current analysed pixel value with the most recent cloud free pixel value.
This method is potentially error-prone as demonstrated in the section :ref:`impact` or explained in :ref:`confusion-matrix`
for the case of the presence of a halo with low values around a cloud. To reduce the error of commission and assure that
a pixel tagged as a cloud is really a cloud, we could proceed like [Cham16]_ and compare the pixel value not only with the last
cloud free pixel value but with all overlapping pixel values of the time series. For each time that the condition of the
blue test if fulfilled, the pixel receives a positive vote and its only classified as a cloud if it receives more than 66% of
the votes.

This idea of using the whole time series for reference values could be also applied to the neighbourhood correlation test.
It was noticed that this test had some problems with the reclassification of pixels in the first images of the time series,
possibly due to the lack of neighbourhoods to use as a reference. We should consider the option of using more images of the time
series as a reference for the neighbourhood correlation test, including the images that are posterior in time and not only the 10
previous images. This modification should have a stronger positive impact in the case of running the algorithm on short time series.

The two suggested modifications corresponding to the blue and to the neighbourhood correlation test follow the aim to
reduce the error of commission. Another way to assure that only cloudy pixels are detected is to increase the value of the blue parameter
(compare with :ref:`fig-blue`). This would certainly raise the error of omission, since the thin clouds and, especially,
the cloud edges, would not be detected. To deal with this matter we propose the following approach:
First, run the blue test with a blue parameter value that allows the classification of thick clouds, but lets out the
thin clouds and, most important, the bright surfaces that are not clouds. It is important that only clouds are detected
in this step before we continue to the next: the delineation of the edges of the clouds using a region growing approach.
This methodology described by [SKSK11]_ combines pixel-based cloud identification with object-based region growing.
Other authors also use the region growing algorithm to refine their results [Cham16]_. The groups
of pixels identified as clouds by the high threshold of the blue test are the initial patches for the posterior region
growing process. For each one of these pixel groups, the average and the standard deviation of the reflectance values in the
blue band are calculated. These values are then used as a reference for the region growing process, which aggregates to the
cloud region the pixels within an 8-neighbourhood that not depart from the computed average more than 2.5 times the standard deviation.
This approach permits detecting thin clouds with lower reflectance values in relation to their proximity to thicker
clouds. It is considered that combining this region growing process with other classification methods improves the results of the
latter [SKSK11]_. The only drawback is the omission of thin clouds that are not located near a thick cloud. At this point,
we will mention that some authors consider unnecessary to mask thin clouds out if the surface spatial variability is
still detectable [LyWF08]_.

These modifications of the existing tests and the implementation of new methods should ameliorate the results of the
multi-temporal cloud detection algorithm. Still, the limitations are given by the characteristics of the satellite, particularly
the absence of a thermal band. On the other hand, the high temporal resolution of RapidEye allows the creation of time
series with images that are very near in time. This type of time series would lead to better cloud masks when running the
algorithm, since the reflectance values would change slowly from one image to the next, except in the presence of clouds.

The condition of a first cloud-free image to begin the algorithm is not convenient for a method supposed to identify
clouds automatically. [HHVD10]_ suggest the next solution: to obtain the first cloud-free reference by a simple threshold on
the blue band reflectance. The cloud-free references for the pixels tagged as a cloud in this first image can be simply taken from
another image using the same system. A pixel mosaic with cloud-free pixel values can be created following this approach.

The lack of efficiency of the code due to the long execution time of the algorithm was already referred at the beginning
of this section. Some ideas for improving the efficiency are now presented. First, the :ref:`import-image` function
imports the reflectance values for all the pixels in the images for the blue and for the red band to a dictionary. Instead
of this, a :ref:`multi-temp` test accessing each pixel value at the needed time would be a more efficient variant.

The second alternative to reduce the processing time would be to minimize the number of pixels where the :ref:`red-blue` and
the :ref:`neigh-cor` are run. This latter test takes particularly computational effort as it works with a neighbourhood array
of reflectance values for each date instead of a unique value. Therefore, we propose that if a pixel is already reclassified
as cloud-free by the red-blue test, the neighbourhood correlation test is not executed for this pixel. This
simple modification was not implemented in our algorithm because we were interested in observing under which conditions
each one of the two tests was responsible for the reclassification of a pixel, including the cases when both reclassified
the pixel. In addition, the latter mentioned cases didn't occur with high frequency in our algorithm due to the low influence
of the red-blue test in the results. Therefore, this modification wouldn't have improved the speed of the algorithm under
the current conditions but should be kept in mind for future versions.

A similar approach would be a progressive refinement of the results, where the output of the :ref:`multi-temp` are not
limited to cloud, cloud-free or not data, but include a "not sure" possibility in the case that the reflectance increase
is only slightly above the threshold of the :ref:`blue-test`. The reclassifying tests are then only run on pixels with this label.

The last proposed alternative used in cases of high computational complexity is a parallel computing approach [KKKS07]_.
This option should be considered for large images or very long time series.

Finally, the aforementioned problem with cloud shadows in the section :ref:`reference-pixels` affects not only the
correct identification of clouds, but they also represent an additional obstacle for remote sensing applications by
distorting the surface reflectance values. For this reason, shadow pixels are often masked and sometimes cloud detection
algorithms include shadow detection [HeCy09]_ [ZCWH12]_ [BrWZ15]_ [Cham16]_. The development or implementation of a cloud
mask would complete the algorithm and improve the results of the cloud masks, but it falls out of the scope of this project.

