
na_matrix = np.full((3,3), np.nan)

size = 3
row, col = 526, 718  # for image

date_ref = [key for key in dictionary_blue_red["blue"].keys()][0]
date = [key for key in dictionary_blue_red["blue"].keys()][1]

np.put(na_matrix, [value for value in range(na_matrix.shape[0] ** 2)], [y for y in range(0, 9)])

###################


