import datetime
from src.timeseries import extract_timeseries
import pandas as pd
import numpy as np


# Test 1 #
def mtcd_test1(dic, row, col):
    # test if the temporal variation of reflectance on the blue band is big compared to a threshold
    # Big increase indicates cloud

    time_series_blue = extract_timeseries(dic, "blue", row, col)
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


# Test 2 #
def mtcd_test2(dic, row, col):
    # test if the variation of reflectance in the red band is much greater than in the blue band

    time_series_red = extract_timeseries(dic, "red", row, col)
    data_frame_red = pd.DataFrame(time_series_red)  # creates a data frame

    refl_red_dayref = data_frame_red["values"][0]  # extracts the pixel value of the reference image
    refl_red_dayd = data_frame_red["values"][1]  # extracts the pixel value of an image

    dayd = datetime.datetime.strptime(data_frame_red["dates"][0], "%Y-%m-%d")  # extracts the date value
    dayref = datetime.datetime.strptime(data_frame_red["dates"][1],
                                        "%Y-%m-%d")  # extracts data value of reference image

    if (refl_red_dayd - refl_red_dayref) > 150 * (dayd - dayref).total_seconds() / (60 * 60 * 24):
        return False
    else:
        return True


# Test 3 #
def mtcd_test3(dic, band, row, col):
    # test if the reflectance in the pixel neighborhood is well correlated with those of the same neighborhood in
    # another image
    up = row - 1
    down = row + 1
    right = col + 1
    left = col - 1

    date_ref = [key for key in dic[band].keys()][0]
    date = [key for key in dic[band].keys()][1]

    if row == 0:
        d = dic[band][date][row, left]
        e = dic[band][date][row, col]
        f = dic[band][date][row, right]
        g = dic[band][date][down, left]
        h = dic[band][date][down, col]
        i = dic[band][date][down, right]
        D = dic[band][date_ref][row, left]
        E = dic[band][date_ref][row, col]
        F = dic[band][date_ref][row, right]
        G = dic[band][date_ref][down, left]
        H = dic[band][date_ref][down, col]
        I = dic[band][date_ref][down, right]
        array1 = np.array([[d, e, f], [g, h, i]])
        array2 = np.array([[D, E, F], [G, H, I]])

    elif row == 526:
        a = dic[band][date][up, left]
        b = dic[band][date][up, col]
        c = dic[band][date][up, right]
        d = dic[band][date][row, left]
        e = dic[band][date][row, col]
        f = dic[band][date][row, right]
        A = dic[band][date_ref][up, left]
        B = dic[band][date_ref][up, col]
        C = dic[band][date_ref][up, right]
        D = dic[band][date_ref][row, left]
        E = dic[band][date_ref][row, col]
        F = dic[band][date_ref][row, right]
        array1 = np.array([[a, b, c], [d, e, f]])
        array2 = np.array([[A, B, C], [D, E, F]])

    elif col == 0:
        b = dic[band][date][up, col]
        c = dic[band][date][up, right]
        e = dic[band][date][row, col]
        f = dic[band][date][row, right]
        h = dic[band][date][down, col]
        i = dic[band][date][down, right]
        B = dic[band][date_ref][up, col]
        C = dic[band][date_ref][up, right]
        E = dic[band][date_ref][row, col]
        F = dic[band][date_ref][row, right]
        H = dic[band][date_ref][down, col]
        I = dic[band][date_ref][down, right]
        array1 = np.array([[b, c], [e, f], [h, i]])
        array2 = np.array([[B, C], [E, F], [H, I]])

    elif col == 718:
        a = dic[band][date][up, left]
        b = dic[band][date][up, col]
        d = dic[band][date][row, left]
        e = dic[band][date][row, col]
        g = dic[band][date][down, left]
        h = dic[band][date][down, col]
        A = dic[band][date_ref][up, left]
        B = dic[band][date_ref][up, col]
        D = dic[band][date_ref][row, left]
        E = dic[band][date_ref][row, col]
        G = dic[band][date_ref][down, left]
        H = dic[band][date_ref][down, col]
        array1 = np.array([[a, b], [d, e], [g, h]])
        array2 = np.array([[A, B], [D, E], [G, H]])

    else:
        a = dic[band][date][up, left]
        b = dic[band][date][up, col]
        c = dic[band][date][up, right]
        d = dic[band][date][row, left]
        e = dic[band][date][row, col]
        f = dic[band][date][row, right]
        g = dic[band][date][down, left]
        h = dic[band][date][down, col]
        i = dic[band][date][down, right]

        A = dic[band][date_ref][up, left]
        B = dic[band][date_ref][up, col]
        C = dic[band][date_ref][up, right]
        D = dic[band][date_ref][row, left]
        E = dic[band][date_ref][row, col]
        F = dic[band][date_ref][row, right]
        G = dic[band][date_ref][down, left]
        H = dic[band][date_ref][down, col]
        I = dic[band][date_ref][down, right]
        array1 = np.array([[a, b, c], [d, e, f], [g, h, i]])
        array2 = np.array([[A, B, C], [D, E, F], [G, H, I]])

    cov = np.mean((array1 - array1.mean()) * (array2 - array2.mean()))
    max_cov = array1.std() * array2.std()
    result = cov / max_cov
    return result


