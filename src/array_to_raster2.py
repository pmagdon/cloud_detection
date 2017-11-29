from osgeo import gdal

def array_to_raster(array):
    """Array > Raster
    Save a raster from a C order array.

    :param array: ndarray
    """
    dst_filename = "C:/Users/anpla/PycharmProjects/cloud_detection/raster.tiff"

    # You need to get those values like you did.
    x_pixels = 100  # number of pixels in x
    y_pixels = 100  # number of pixels in y
    PIXEL_SIZE = 5  # size of the pixel...
    x_min = 553648
    y_max = 7784555  # x_min & y_max are like the "top left" corner.

    image = gdal.Open("data/2015-03-19.tif")
    proj = image.GetProjection()

    driver = gdal.GetDriverByName('GTiff')

    dataset = driver.Create(
        dst_filename,
        x_pixels,
        y_pixels,
        1,
        gdal.GDT_Float32, )

    wkt_projection = dataset.SetProjection(proj)

    dataset.SetGeoTransform((
        x_min,    # 0
        PIXEL_SIZE,  # 1
        0,                      # 2
        y_max,    # 3
        0,                      # 4
        -PIXEL_SIZE))

    dataset.SetProjection(wkt_projection)
    dataset.GetRasterBand(1).WriteArray(array)
    dataset.FlushCache()  # Write to disk.
    return dataset, dataset.GetRasterBand(1)  #If you need to return, remenber to return  also the dataset because the band don`t live without dataset