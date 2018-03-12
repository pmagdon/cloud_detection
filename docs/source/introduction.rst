Introduction
============
`Data sets`_

The presence of clouds in satellite imagery obscures the view of Earth surface features(2) and distorts the spectral
information of the surface characteristic of clear-sky images (2). This represent an impediment for remote sensing
applications (7) using automatic processing algorithms (15). For instance, the presence of clouds can cause false change
detections and cause wrong land cover classification. Other cases where cloud presence can be problematic are surface
studies like vegetation monitoring (6) or time series analysis. This leads to reduced accuracy of the map products
created using satellite imagery with cloud presence(2). Therefore, the erroneous values of the cloudy pixels should not
be considered in these analysis (6). Cloud masks cover the pixels that are clouds to exclude their values of the
calculations and avoid biased results as a consequence of these values. As a result, cloud detection and the creation of
cloud masks are an important pre-processing step in remote sensing (2).

The manual masking of clouds is a time-consuming task. The high availability of satellite imagery makes enables multi-
temporal analysis with large amount of images. For this cases, the manual masking of clouds is not an option and the
development of an automatic cloud detection algorithm is important (11).

Many approaches have been applied for the development of efficient cloud detection algorithms. The strategy employed for
each of them is highly dependent on the characteristics of the sensors, but they are mainly based in the use of the common
features of clouds: their reflectance is high in the visible spectral bands, they are cold (9) and connex objects (14).

For satellites with high spectral resolution, a common method to detect clouds is the use of the thermal band. (13)
develops a unique cloud thermal signature for cloud identification and (4) uses the MODIS measurements of brightness
temperature and runs a pixel by pixel test. The values of the water vapor band help to detect high clouds. Other methods
developed for moderate resolution imagery combine the use of the thermal band with tests using other bands, like (9),
where 14 spectral bands are used and different tests are run depending of the scene in the image and the time of the day.
This option is only available to sensors with high spectral resolution.

The segmentation method is based in the determination of the class of a pixel with regard to its neighbourhoods. This
method is applied by (5) and by (8) making use of Markov Random Fields. (3) uses supervised classification and creates
a training set which determines typical reflectance features of clouds and then employs it for cloud detection. Another
option is to make use of the relationship between clouds and their shadows, like 6 and 7, where the cloud identification
is shadow oriented. Shadow pixel are often masked since they represent an obstacle for remote sensing applications, like
clouds. More advanced cloud detection methods make use of machine learning and multi feature fusion to distinguish
clouds from Earth surface (17).

Despite the large number of approaches in the field of cloud detection, there are a smaller number of studies for the
specific case of high resolutions sensors with no thermal band. The reason for this could be that the studies executed
using this type of sensors are commonly focused on smaller areas making a realistic option the manual identification and
delineation of clouds. When this option is not possible and a thermal channel is available, spectral thresholding using
the thermal band has been th common approach (10).

The satellite images that were used to implement the cloud detection algorithm described in this project are provided by
the satellite sensor RapidEye, which has a high spatial resolution but a limited number of bands and no thermal band.
A convenient cloud detection method for these conditions can be found in the literature. (15) develops a multi temporal
cloud detection algorithm on a pixel basis which makes use of a threshold on the reflectance temporal variation in the
blue band to detect clouds. Two other tests are additionally run to assure a correct cloud identification, one of them
using the reflectance values of the red band. The method uses a time series to compare the current pixel value with
a clear sky reference value from a previous image (4). Multi temporal cloud detection algorithms relay on the hypothesis
that the reflectance of an area stays relatively stable in time in cloud free conditions, while in presence of clouds,
the reflectance values highly increase (7).

The satellite RapidEye includes the blue and the red spectral bands, has a high temporal resolution which allows the
creation of a time series and a high spatial resolution which makes it adequate for a pixel by pixel analysis. Taking
this into account, the multi temporal cloud detection algorithm (15) represents a possibility to identify clouds in images
of RapidEye. The objective of this project is the implementation and adaptation of this algorithm using the programming
language Python.
