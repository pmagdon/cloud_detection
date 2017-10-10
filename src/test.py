
def test_3(dic, band, row, col, size):
    na_matrix = np.full((size, size), np.nan)

    date = [key for key in dic[band].keys()][1]

    half = int(size/2 + 0.5 -1)
    row_limit = dic[band][date].shape[0]
    col_limit = dic[band][date].shape[1]

    if row - half > 0 and row + half < row_limit and col - half > 0 and col + half < col_limit:
        np.put(na_matrix, [value for value in range(na_matrix.shape[0] ** 2)],
           dic[band][date][[row for row in range(row-half, row+half)],
                           [col for col in range(col-half, col+half)]])

    return na_matrix

#################################################################################################

def cloud_mask(dic, band, row, col):
    result = mtcd_value(dic, band, row, col)
    date = [key for key in dic[band].keys()][-1]

    dic["band"].update({date: result})  # nicht update sondern sustituir/überschreiben

####################################################################################################

na_matrix = np.full((3,3), np.nan)

size = 3
row, col = 526, 718  # for image

date_ref = [key for key in dictionary_blue_red["blue"].keys()][0]
date = [key for key in dictionary_blue_red["blue"].keys()][1]

np.put(na_matrix, [value for value in range(na_matrix.shape[0] ** 2)], [y for y in range(0, 9)])



