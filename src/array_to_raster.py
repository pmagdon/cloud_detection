import gdal, osr
import rasterio


def array2raster(im_source, fname_nraster, pixel_width, pixel_height, dict, date):
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

    print("Array converted to raster")



