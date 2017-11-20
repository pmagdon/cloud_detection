import gdal, ogr, os, osr

############## 1 Versuch ####################

# Source: https://stackoverflow.com/questions/37648439/simplest-way-to-save-array-into-raster-file-in-python #####
dst_filename = 'cloud_mask3.tiff'
x_pixels = 100  # number of pixels in x
y_pixels = 100  # number of pixels in y
driver = gdal.GetDriverByName('GTiff')
dataset = driver.Create(dst_filename,100, 100, 1,gdal.GDT_Float32)
outds = dataset.GetRasterBand(1).WriteArray(cloud_mask_array)
## this first part works, the file is created, but I can't open it, I think because is without reference

image = gdal.Open("data/2015-03-19.tif")

# follow code is adding GeoTranform and Projection
geotrans= image.GetGeoTransform()  #get GeoTranform from existed 'data0'
proj=image.GetProjection() #you can get from a exsited tif or import
outds.SetGeoTransform(geotrans)
outds.SetProjection(proj)
outds.FlushCache()
outds=None
## my problem: what is outds? i imagine it refers to output dataset, but I'm not sure what I have to write there

################## 2 Versuch ###########################################################
# Source: https://pcjericks.github.io/py-gdalogr-cookbook/raster_layers.html
im = gdal.Open("data/2015-04-09.tif")

array2raster('cloud_mask.tiff', values, 5, 5, cloud_mask_array)

def array2raster(newRasterfn,rasterOrigin,pixelWidth,pixelHeight,array):

    cols = array.shape[1]
    rows = array.shape[0]
    originX = rasterOrigin[0]
    originY = rasterOrigin[1]

    driver = gdal.GetDriverByName('GTiff')
    outRaster = driver.Create(newRasterfn, cols, rows, 1, gdal.GDT_Byte)
    outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
    outband = outRaster.GetRasterBand(1)
    outband.WriteArray(array)
    outRasterSRS = osr.SpatialReference()
    outRasterSRS.ImportFromEPSG(4326)
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()

# my problem: the parameter "Raster origin" . I imagine it refers to the coordinates of the pixel of origin, which I
# tried to get with help of the next function, aber ich misstraue die Ergebnisse...

def pixel(file, dx,dy):
    px = file.GetGeoTransform()[0]
    py = file.GetGeoTransform()[3]
    rx = file.GetGeoTransform()[1]
    ry = file.GetGeoTransform()[5]
    x = dx/rx + px
    y = dy/ry + py
    return x,y

values = pixel(image, 0, 0)

# At some point I managed to open one raster that I created with qgis, but the values were 0 or na and it didn't show
# anything...