import datetime


def mtcd_value(dic, band, row, col):
    # check the result of the 3 tests and returns
    # True when cloud, value of the pixel when not cloud
    time_series = extract_timeseries(dic, band, row, col)
    refl_dayd = time_series["values"][-1]

    Test_1 = mtcd_test1(dic, row, col)
    Test_2 = mtcd_test2(dic, row, col)
    Test_3 = mtcd_test3(dic, band, row, col)

    if Test_1 == True and Test_2 == False and Test_3 == False:
        return False
    else:
        return refl_dayd

def cloud_mask(dic, band, row, col):
    result = mtcd_value(dic, band, row, col)
    date = [key for key in dic[band].keys()][-1]

    dic["band"].update({date: result})  # nicht update sondern sustituir/überschreiben
####################################################################################################

import rasterio

def expand_image(file, band):
    old_im = rasterio.open(file)
    old_im = old_im.read(band)
    old_size = old_im.shape
    new_row = old_size[0]+ 10
    new_col = old_size[1] + 10
    new_size = (new_row, new_col)
    new_im = np.full((new_row, new_col), np.nan)
    im_nan = new_im.paste(old_im, (new_size[0] - old_size[0])/2,
                          (new_size[1] - old_size[1])/2)
    return im_nan

old_im = Image.open('someimage.jpg')
old_size = old_im.size

new_size = (800, 800)
new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
new_im.paste(old_im, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))

new_im.show()
# new_im.save('someimage.jpg')


####################################




np.full((6,2), np.nan)

