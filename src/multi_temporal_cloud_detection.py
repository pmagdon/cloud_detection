import datetime
from src.timeseries import extract_timeseries# why this is not working?
import pandas as pd


def mtcd(dic_blue, dic_red, row, column):
    # tests if a pixel is cloud or clear comparing with a cloud free image

    time_series_blue = extract_timeseries(dic_blue, row, column)
    data_frame_blue = pd.DataFrame(time_series_blue)  # creates a data frame

    time_series_red = extract_timeseries(dic_red, row, column)
    data_frame_red = pd.DataFrame(time_series_red)  # creates a data frame

    refl_blue_dayd = data_frame_blue["values"][0] # extracts the pixel value of an image
    refl_blue_dayref = data_frame_blue["values"][1] # extracts the pixel value of the reference image
    refl_red_dayd = data_frame_red["values"][0]
    refl_red_dayref = data_frame_red["values"][1]
    dayd = datetime.datetime.strptime(data_frame_blue["dates"][0], "%Y-%m-%d")  # extracts the date value
    dayref = datetime.datetime.strptime(data_frame_blue["dates"][1], "%Y-%m-%d")  # extracts data value of reference image

    if abs(refl_blue_dayd - refl_blue_dayref) > 3 * (
        1 + (dayd - dayref).total_seconds() / (60 * 60 * 24) / 30) and \
            (refl_red_dayd - refl_red_dayref) < 150 * (abs(dayd - dayref).total_seconds() / (60 * 60 * 24)):
        return True
    else:
        return False


# why absolute values for difference? in the case that we have non cloud-cloud: that should be also noted as change

# A pixel that verifies equation 1 is finally not flagged as cloudy if any of the following 2 conditions is true:
# if the variation of reflectance in the red band is uch greater than in the blue band
# if the reflectance in the pixel neighborhood are well correlated with those of the same neighborhood in one of the ten
# images acquired before the date (or maybe just with 2: before and after)

# Gedanken:
# Mit der anderen Methode (automatic detection of clouds)
# eine cloud free image suchen bzw. bauen und dann weiter hiermit arbeiten
# Denn die erste Methode ist schneller, man vergleicht nur zwischen 1 Bild und 1 cloud free und nicht alle Bilder
# miteinander



