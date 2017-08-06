import datetime
from timeseries import extract_timeseries # why this is not working?



def mtcd(dic, row, column):
    # tests if a pixel is cloud or clear comparing with a cloud free image

    time_series = extract_timeseries(dic, row, column)
    data_frame = pd.DataFrame(time_series)  # creates a dataframe

    refl_blue_dayD = data_frame["values"][0] # extracts the pixel value of an image
    refl_blue_dayref = data_frame["values"][1] # extracts the pixel value of the reference image
    refl_red_dayD = data_frame["values"][0]
    refl_red_dayref = data_frame["values"][1]
    dayD = datetime.datetime.strptime(data_frame["dates"][0], "%Y-%m-%d")  # extracts the date value
    dayref = datetime.datetime.strptime(data_frame["dates"][1], "%Y-%m-%d")  # extracts data value of reference image

    if abs(refl_blue_dayD - refl_blue_dayref) > 0.03 * (
        1 + abs(dayD - dayref).total_seconds() / (60 * 60 * 24) / 30) and \
                    abs(refl_red_dayD - refl_red_dayref) > 1.5 * (abs(dayD - dayref).total_seconds() / (60 * 60 * 24)):
        return "change"
    else:
        return "no change"



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



