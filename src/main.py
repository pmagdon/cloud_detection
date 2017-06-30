import numpy as np
from src.import_image import import_image




# 1. Test: import_image function

dictionary = {}
image_file_1 = 'data/clip1.tif'
image_file_2 = 'data/clip2.tif'
import_image(image_file_1, 1, dictionary)
import_image(image_file_2, 1, dictionary)


# 2. Test: easy dictionary

x = np.matrix("1 2 3; 4 5 6")
y = np.matrix("7 8 9; 10 11 12")

d = {"a" : x, "b": y}

def timeseries(dic):
    for x in range(0,2):
        for y in range(0,3):
            print([value[x, y] for value in dic.values()])

 [value[0,0] for value in d.values()]


# 3. Test: time series functions that I will not use

def extract_timeseries(dic):
    # a bit more useful, because the number row and column is integrated,
    # but only specific for this picture size...
    for x in range(0,528):
        for y in range(0,720):
            print([value[x, y] for value in dic.values()])


def extract_timeseries(dic):
    # prints lists of pairs of values with the same position in a dictionary
    # that contains matrix. also prints class and dictionary keys
    row = next(len(i) for i in dic.values()) - 1
    col = next(i.shape[1] for i in dic.values()) - 1
    for x in range(0, row):
        for y in range(0,col):
            print([value[x, y] for value in dic.values()])
            print(type([value[x, y] for value in dic.values()]))
            print(dic.keys())

def get_keys(dic):
    # prints the keys of the dictionary (in this case the date info)
    # for so many times as values in the matrix (in this case pixels)
    row = next(len(i) for i in dic.values()) + 1
    col = next(i.shape[1] for i in dic.values()) + 1
    for i in range(0, row * col + 1):
        print(dic.keys())



