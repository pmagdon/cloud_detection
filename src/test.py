import datetime
import pandas as pd
from timeseries import extract_timeseries # why this is not working?

def mtcd_blue(dic, row, column):
    # test if the difference of pixel value between a reference image and a cloud free image in blue band is greater
    # than 3% (corrected by difference in the dates)
    # dataframe with the values of one pixel over different dates
    # we don't have a cloud free image like in the paper but
    # we still can use this as a change/no_change function
    time_series = extract_timeseries(dic, row, column)
    data_frame = pd.DataFrame(time_series)  # creates a dataframe

    refl_blue_dayD = data_frame["values"][0] # extracts the pixel value of an image
    refl_blue_dayref = data_frame["values"][1] # extracts the pixel value of the reference image
    dayD = datetime.datetime.strptime(data_frame["dates"][0], "%Y-%m-%d") # extracts the date value
    dayref = datetime.datetime.strptime(data_frame["dates"][1], "%Y-%m-%d")# extracts the data value of the reference image

    if abs(refl_blue_dayD - refl_blue_dayref) > 0.03 * (1 + abs(dayD - dayref).total_seconds() / (60 * 60 * 24) / 30):
        return "change"
    else:
        return "no change"
