import datetime

def mtcd_blue(dataframe):
    # test if the difference of pixel value between a reference image and a cloud free image in blue band is greater
    # than 3% (corrected by difference in the dates)
    # dataframe with the values of one pixel over different dates
    # we don't have a cloud free image like in the paper but
    # we still can use this as a change/no_change function
    refl_blue_dayD = dataframe["values"][0] # extracts the pixel value of an image
    refl_blue_dayref = dataframe["values"][1] # extracts the pixel value of the reference image
    dayD = datetime.datetime.strptime(dataframe["dates"][0], "%Y-%m-%d") # extracts the date value
    dayref = datetime.datetime.strptime(dataframe["dates"][1], "%Y-%m-%d")# extracts the data value of the reference image

    if abs(refl_blue_dayD - refl_blue_dayref) > 0.03*(1+abs(dayD - dayref).total_seconds()/(60*60*24)/30):
        return "change"
    else:
        return "no change"


    # why absolute values for difference? in the case that we have non cloud-cloud: that should be also noted as change

# A pixel that verifies equation 1 is finally not flagged as cloudy if any of the following 2 conditions is true:
# if the variation of reflectance in the red band is uch greater than in the blue band
# if the reflectance in the pixel neighborhood are well correlated with those of the same neighborhood in one of the ten
# images acquired before the date (or maybe just with 2: before and after)

# Gedanken: macht überhaupt Sinn eine change no change function zu haben?
# Die andere Option ist mit der anderen Methode (automatic detection of clouds)
# eine cloud free image zu suchen bzw. zu bauen und dann weiter hiermit arbeiten
# Denn die erste Methode ist schneller, man kann viele Bilder auf einmal testen und nicht 1 für 1

# Andere Gedanken: wollen wir als input von mtcd function 2 Bilder haben und als output nur: change/nochange
# oder lieber alle Bilder als input, jedes Bildpaar vergleichen und als output eine list aus change/nochange



