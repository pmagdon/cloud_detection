import rasterio


def import_image(file, blue_band, red_band, dic):
    """
        Reads the image file, takes the values of the selected bands
        and of the acquisition time and updates a nested dictionary with them

    :param str file: The inputfile.
    :param int blue_band: The number of the blue band.
    :param object dict:

    :return bool test: The return value. True for success, False otherwise.

    """

    im = rasterio.open(file)
    im_blue_band = im.read(blue_band)
    im_red_band = im.read(red_band)
    date = im.tags()['Acquisition_DateTime'][0:10]
    dic["blue"].update({date: im_blue_band})
    dic["red"].update({date: im_red_band})
    print("Dictionary updated")

def import_cloudfree_reference(file, dic):
    first_ref_values = rasterio.open(file).read(1)
    date_first_ref = rasterio.open(file).tags()['Acquisition_DateTime'][0:10]
    first_ref_mask = np.full_like(first_ref_values, True)
    dic.update({date_first_ref: first_ref_mask})
    print("First cloud free reference imported to dictionary")


