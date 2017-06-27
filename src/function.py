import rasterio
def import_image(file, band, dict):
    # "Reads the image file, takes the values of the selected band
    # and of the acquisition time and updates a dictionary with them"
    im = rasterio.open(file)
    imb = im.read(band)
    date = im.tags()['Acquisition_DateTime']
    dict.update({date: imb})
    print("Dictionary updated")
    return 1

dictionary = {}

tmp = import_image('clip1.tif',1,dictionary)




