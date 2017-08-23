import datetime
from src.timeseries import extract_timeseries
import pandas as pd



def mtcd_test1(dic, row, column):
    # test if the temporal variation of reflectance on the blue band is big compared to a threshold
    # Big increase indicates cloud

    time_series_blue = extract_timeseries(dic, "blue", row, column)
    data_frame_blue = pd.DataFrame(time_series_blue)  # creates a data frame

    refl_blue_dayref = data_frame_blue["values"][0]  # extracts the pixel value of the reference image
    refl_blue_dayd = data_frame_blue["values"][1] # extracts the pixel value of an image

    dayd = datetime.datetime.strptime(data_frame_blue["dates"][0], "%Y-%m-%d")  # extracts the date value
    dayref = datetime.datetime.strptime(data_frame_blue["dates"][1], "%Y-%m-%d")  # extracts data value of reference image

    if refl_blue_dayd - refl_blue_dayref > 3 * (
        1 + (dayd - dayref).total_seconds() / (60 * 60 * 24) / 30):
        return True
    else:
        return False


def mtcd_test2(dic, row, column):
    time_series_red = extract_timeseries(dic, "red", row, column)
    data_frame_red = pd.DataFrame(time_series_red)  # creates a data frame

    refl_red_dayref = data_frame_red["values"][0]  # extracts the pixel value of the reference image
    refl_red_dayd = data_frame_red["values"][1]  # extracts the pixel value of an image

    dayd = datetime.datetime.strptime(data_frame_red["dates"][0], "%Y-%m-%d")  # extracts the date value
    dayref = datetime.datetime.strptime(data_frame_red["dates"][1],
                                        "%Y-%m-%d")  # extracts data value of reference image

    if (refl_red_dayd - refl_red_dayref) > 150 * (dayd - dayref).total_seconds() / (60 * 60 * 24)
        return False
    else:
        return True

def mtcd_test3

# Test 2: A pixel that verifies equation 1 is finally not flagged as cloudy if any of the following 2 conditions is true:
# if the variation of reflectance in the red band is much greater than in the blue band
# Test 3: if the reflectance in the pixel neighborhood are well correlated with those of the same neighborhood in one of
#  the ten images acquired before the date (or maybe just with 2: before and after)