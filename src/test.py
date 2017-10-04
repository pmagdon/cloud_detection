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

def test_3(dic, band, row, col, size):
    up = row - 1
    down = row + 1
    right = col + 1
    left = col - 1

####################
na_matrix = np.full((3,3), np.nan)

size = 3
row, col = 526, 718  # for image

date_ref = [key for key in dictionary_blue_red["blue"].keys()][0]
date = [key for key in dictionary_blue_red["blue"].keys()][1]

def test_3(dic, band, row, col):

    na_matrix = np.full((3, 3), np.nan)

    date = [key for key in dic[band].keys()][1]

    def index_error(index, row_im, col_im):
        try:
            np.put(na_matrix, [index], dic[band][date][row_im, col_im])
        except IndexError: na_matrix

    index_error(4, row, col)
    index_error(5, row, col+1)
    index_error(7, row+1, col)
    index_error(8, row+1, col+1)

    if row - 1 >= 0:
        index_error(0, row-1, col-1)
        index_error(1, row - 1, col)
        index_error(2, row - 1, col + 1)
    else: na_matrix

    if col -1>=0:
        index_error(3, row, col-1)
        index_error(6, row+1, col-1)
    else: na_matrix


##############################


try:
    na_matrix[mid - 1, mid - 1] = dictionary_blue_red["blue"][date][row - 1, col - 1]
except IndexError:
    na_matrix

if row - 1 < 0: na_matrix[mid - 1, mid - 1] = np.nan

try:
    na_matrix[mid - 1, mid] = dictionary_blue_red["blue"][date][row - 1, col]
except IndexError:
    na_matrix[mid - 1, mid] = np.nan
if row -1 < 0: na_matrix[mid - 1, mid] = np.nan

try:
    na_matrix[mid - 1, mid + 1] = dictionary_blue_red["blue"][date][row - 1, col + 1]
except IndexError:
    na_matrix[mid - 1, mid + 1] = np.nan
if row-1 < 0: na_matrix[mid - 1, mid + 1] = np.nan

try:
    na_matrix[mid, mid - 1] = dictionary_blue_red["blue"][date][row, col - 1]
except IndexError:
    na_matrix[mid, mid - 1] = np.nan
if col - 1 < 0 : na_matrix[mid, mid - 1] = np.nan

try:
    na_matrix[mid, mid + 1] = dictionary_blue_red["blue"][date][row, col + 1]
except IndexError:
    na_matrix[mid, mid + 1] = np.nan

try:
    na_matrix[mid + 1, mid - 1] = dictionary_blue_red["blue"][date][row + 1, col - 1]
except IndexError:
    na_matrix[mid + 1, mid - 1] = np.nan
if col -1 < 0: na_matrix[mid + 1, mid - 1] = np.nan

try:
    na_matrix[mid + 1, mid] = dictionary_blue_red["blue"][date][row + 1, col]
except IndexError:
    na_matrix[mid + 1, mid] = np.nan

try:
    na_matrix[mid + 1 , mid + 1] = dictionary_blue_red["blue"][date][row + 1, col + 1]
except IndexError:
    na_matrix[mid + 1, mid + 1] = np.nan




####################

a=['123','2',4]
index = -1

try:
    b = a[index]
except IndexError:
    b = np.nan

a=['123','2',4]
index = -1
if index < 0: b = np.nan
