Introduction
=============
What is cloud detection and why do we need a cloud mask?
Nowadays there is a high availability of satellite imagery and very often it can be freely downloaded from the internet.
Contar que hay varios satélites con diferente tamaño de pixel y numero de bandas y que cada banda corresponde a un
intervalo del espectro y que, en la imagen, después de la corrección atmosférica, tenemos el porcentaje de reflexión de
la superficie terrestre en cada una de las bandas.

Though, these images need a pre-processing step before the actual analysis begins. This is the case if there are clouds
on them, which occurs quite regularly. Clouds not only cover the earth surface, wherein we are interested, but they
also modify the reflectance values, which, when running the analysis, will lead to incorrect results.
Examples of analysis: classification, change detection.
Therefore, it is very useful to have a cloud mask, which covers the pixels that are clouds to exclude these pixels of
the analysis. On this way, the calculations ignore the masked pixels and the result of the analysis is not biased by
the values of the cloud pixels.
Large data requires automatic cloud detection algorithm. Examples of large data: time series.
First, we need to identify these pixels.
Easiest way to detect the clouds is with the thermal band. Clouds are colder than the earth surface. Search literature
referring to this and explain more about the thermal band.
When no thermal band available, use other characteristics of the clouds that are available. Working with RapidEye. Tell
more about RapidEye. http://www.biodiversity-exploratories.de/infrastruktur/messtechnik-fernerkundung/
(satellite characteristics)

