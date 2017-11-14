import numpy as np

test_dic = {"cero": np.matrix([[0,0],[np.nan, np.nan]]), "uno": np.full((3, 3), 1, int),
            "dos":  np.full((3, 3), np.nan), "tres": np.full((3,3), 3, int)}

def find_reference_date(dictionary, date):
    # prints all values that are not the given one
    for key, value in dictionary.items():
        if key not in date:
            print(key)

# why it doesn't work with return?