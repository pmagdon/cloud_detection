import gdal
import osr
import rasterio


def array2raster(im_source, fname_nraster, pixel_width, pixel_height, dict, date):
    """
    Create a raster file with one band based in an array stored in a dictionary.

    Source: https://pcjericks.github.io/py-gdalogr-cookbook/raster_layers.html.
    Open the image and read the image bounds to define the origin in x and y for the output raster. Access the array of
    the given date, reverse it so that the tif looks like the array and store its shape. Fetch a driver based on the
    short name GTiff and create a new dataset with this  driver. The size of this dataset corresponds to the shape of
    the array. The number of bands is set to 1. Convert the pixel coordinates to map coordinates using the affine
    transformation. This transformation needs information about the size of the pixel (width and height) and about the
    image bounds (origin in x and in y). Write the array in the band of the created dataset. Set the coordinate system
    and the projection reference for this dataset.

    :param str im_source: The file path of the image to which the cloud mask belongs.
    :param str fname_nraster: The file name of the created raster.
    :param int pixel_width: The pixel width of the image.
    :param int pixel_height: The pixel height of the image.
    :param object dict: The dictionary where the cloud mask is stored.
    :param str date: The date of the image which cloud mask is converted to raster.
    :return: Print the message "Array converted to raster".
    """
    image = rasterio.open(im_source)
    bounds = image.bounds

    array = dict[date]
    reversed_arr = array[::-1] # reverse array so the tif looks like the array
    cols = reversed_arr.shape[1]
    rows = reversed_arr.shape[0]

    originX = bounds[0]
    originY = bounds[1]

    driver = gdal.GetDriverByName('GTiff')
    outRaster = driver.Create(fname_nraster, cols, rows, 1, gdal.GDT_Byte)
    outRaster.SetGeoTransform((originX, pixel_width, 0, originY, 0, pixel_height))
    outband = outRaster.GetRasterBand(1)
    outband.WriteArray(reversed_arr)

    outRasterSRS = osr.SpatialReference()
    outRasterSRS.ImportFromEPSG(32632)
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()
    #outband.Close

    print("Array converted to raster")


def array2raster_3b(im_source, fname_nraster, pixel_width, pixel_height, dict, date, nbands=3):
    """
    Create a raster file with three bands based in an array stored in a dictionary.

    Source: https://pcjericks.github.io/py-gdalogr-cookbook/raster_layers.html.
    Open the image and read the image bounds to define the origin in x and y for the output raster. Access one of the
    three arrays and store its shape. Fetch a driver based on the short name GTiff and create a new dataset with this
    driver. The size of this dataset corresponds to the shape of the arrays. The number of bands is set to 3. Convert
    the pixel coordinates to map coordinates using the affine transformation. This transformation needs information
    about the size of the pixel (width and height) and about the image bounds (origin in x and in y). Reverse all three
    arrays so that the tif looks like the arrays and write the three arrays into a list. Write each array in one diffe-
    rent band of the created dataset. Set the coordinate system and the projection reference for this dataset.

    :param str im_source: The file path of the image to which the cloud mask belongs.
    :param str fname_nraster: The file name of the created raster.
    :param int pixel_width: The pixel width of the image.
    :param int pixel_height: The pixel height of the image.
    :param object dict: The dictionary where the cloud mask is stored.
    :param str date: The date of the image which cloud mask is converted to raster.
    :param str nbands: The number of bands of the raster, the standard value is 3.
    :return: Print the message "3D array converted to multiband raster".
    """
    image = rasterio.open(im_source)
    bounds = image.bounds
    originX = bounds[0]
    originY = bounds[1]

    array_3d = dict[date]
    rows = array_3d[0].shape[0]
    cols = array_3d[0].shape[1]

    driver = gdal.GetDriverByName('GTiff')
    outRaster = driver.Create(fname_nraster, cols, rows, 3, gdal.GDT_Byte)
    outRaster.SetGeoTransform((originX, pixel_width, 0, originY, 0, pixel_height))

    arrays = []
    for band in range(nbands):
        array = dict[date][band]
        reversed_arr = array[::-1]  # reverse array so the tif looks like the array
        arrays.append(reversed_arr)

    outband_1 = outRaster.GetRasterBand(1)
    outband_2 = outRaster.GetRasterBand(2)
    outband_3 = outRaster.GetRasterBand(3)

    outband_1.WriteArray(arrays[0])
    outband_2.WriteArray(arrays[1])
    outband_3.WriteArray(arrays[2])

    outRasterSRS = osr.SpatialReference()
    outRasterSRS.ImportFromEPSG(32632)
    outRaster.SetProjection(outRasterSRS.ExportToWkt())

    outband_1.FlushCache()
    outband_2.FlushCache()
    outband_3.FlushCache()

    print("3D array converted to multiband raster")
