import gdal, osr
import rasterio


def array2raster(im_source, fname_nraster, pixel_width, pixel_height, dict, date, nbands = 3):
    """
    Convert an array stored in a dictionary into a raster file.

    Source: https://pcjericks.github.io/py-gdalogr-cookbook/raster_layers.html

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

    array = dict[date][band]
    reversed_arr = array[::-1] # reverse array so the tif looks like the array
    cols = reversed_arr.shape[1] # Muss angepasst werden an 3D array
    rows = reversed_arr.shape[0]

    originX = bounds[0]
    originY = bounds[1]

    driver = gdal.GetDriverByName('GTiff')
    outRaster = driver.Create(fname_nraster, cols, rows, 3, gdal.GDT_Byte)
    outRaster.SetGeoTransform((originX, pixel_width, 0, originY, 0, pixel_height))
    outband = outRaster.GetRasterBand(1)
    outband.WriteArray(reversed_arr)

    outRasterSRS = osr.SpatialReference()
    outRasterSRS.ImportFromEPSG(32632)
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()

    print("Array converted to raster")

    def array2raster_3b(im_source, fname_nraster, pixel_width, pixel_height, dict, date, nbands=3):
        """
        Convert an array stored in a dictionary into a raster file.

        Source: https://pcjericks.github.io/py-gdalogr-cookbook/raster_layers.html

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
        originX = bounds[0]
        originY = bounds[1]

        array_3d = dict[date]
        rows = array_3d[0].shape[0]
        cols = array_3d[0].shape[1]

        driver = gdal.GetDriverByName('GTiff')
        outRaster = driver.Create(fname_nraster, cols, rows, 3, gdal.GDT_Byte)
        outRaster.SetGeoTransform((originX, pixel_width, 0, originY, 0, pixel_height))

        arrays = []
        bands = []
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

        print("Array converted to raster")
