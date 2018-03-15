************
Introduction
************

The presence of clouds in satellite imagery obscures the view of Earth surface features and distorts the spectral
information of the surface characteristic of clear-sky images [BrWZ15]_. This represents an impediment for remote sensing
applications [ZCWH12]_ using automatic processing algorithms [HHVD10]_. For instance, the presence of clouds can cause false change
detections or wrong land cover classification. Other cases where cloud presence can be problematic are surface
studies like vegetation monitoring [HeCy09]_ or time-series analysis. This leads to a reduced accuracy of the map products
created using satellite imagery with cloud presence [BrWZ15]_. To avoid biased results, the erroneous values of the cloudy pixels should
not be considered in these analysis [HeCy09]_. For excluding these values from the calculations, cloud masks are employed.
An example of a cloud mask can be a raster file with boolean values: True for clear sky pixels and False for cloudy pixels. By multiplying
a satellite image with this cloud mask file, only the cloud-free values remain in the image. Taking all this into account,
we conclude that cloud detection and the creation of cloud masks are an important pre-processing step in remote sensing [BrWZ15]_.

Many approaches have been implemented to develop an efficient cloud detection algorithm. The strategy employed for each
of them is highly dependent on the
characteristics of the sensors, but they are mainly based on the use of the common features of clouds: their reflectance
is high in the visible spectral bands, they are cold [FALS08]_ and connex objects [Cham12]_.

For satellites with high spectral resolution, a common method to detect clouds is spectral thresholding using
the thermal band [SKSK11]_. [Iris00]_ develops a unique cloud thermal signature for cloud identification and [LyWF08]_ uses the MODIS measurements of brightness
temperature and runs a pixel by pixel test. Other methods
developed for moderate resolution imagery combine the use of the thermal band with tests using other bands, like [FALS08]_,
where 14 spectral bands are used and different tests are run depending on the scene in the image and the time of the day.
[ZhXi14]_ and [KKKS07]_ make use of Markov Random Fields in the segmentation method, which detects the class of a pixel with
regard to its neighbourhoods. [HCRI96]_ uses supervised classification and creates
a training set which determines typical reflectance features of clouds and then employs it for cloud detection. Another
option is to make use of the relationship between clouds and their shadows, like [HeCy09]_ and [ZCWH12]_, where the cloud identification
is shadow oriented. More advanced cloud detection methods make use of machine learning and multi-feature fusion to distinguish
clouds from Earth surface [BDKY16]_.

Despite a large number of approaches in the field of cloud detection, there are a smaller number of studies for the
specific case of high resolutions sensors with no thermal band. The reason for this could be that the studies executed
using this type of sensors were commonly focused on smaller areas making the time consuming task of manual identification
and delineation of clouds a realistic option. Currently, we find ourselves in a new scenario with a growing number of
high-resolution satellites and a high availability of satellite imagery. This situation enables the
creation of land cover mapping for large areas or of multi-temporal analysis with a big number of images. For these cases,
the manual masking of clouds is not an option and an automatic cloud detection algorithm is necessary [SMWW17]_
Since many of these sensors don't include the thermal band, there exists a need for the development of cloud identification
methods without the use of this band. These new algorithms should also be able to work with large amounts of data of
high spatial resolution [SKSK11]_.

The available satellite images  for this project are provided by the satellite sensor RapidEye, which has a high spatial
resolution but a limited number of bands and no thermal band (see: :ref:`Data-sets`).
A convenient cloud detection method for these conditions can be found in the literature. [HHVD10]_ develops a multi-temporal
cloud detection algorithm on a pixel basis which makes use of a threshold on the reflectance temporal variation in the
blue band to distinguish clouds from the surface. Two other tests are additionally run to assure a correct cloud identification, one of them
using the reflectance values of the red band. The method uses a time-series to compare the current pixel value with
a clear sky reference value from a previous image [LyWF08]_. Multi-temporal cloud detection algorithms rely on the hypothesis
that the reflectance of an area stays relatively stable in time in cloud-free conditions, while in presence of clouds,
the reflectance values highly increase [ZCWH12]_.

The satellite RapidEye includes the blue and the red spectral bands, has a high temporal resolution which allows the
creation of a time-series and a high spatial resolution which makes it adequate for a pixel by pixel analysis (see :ref:`Data-sets`).
Taking this into account, the multi-temporal cloud detection algorithm [HHVD10]_ represents a possibility to identify clouds in images
of RapidEye. The objective of this project is the implementation and adaptation of this algorithm using the programming
language Python.

