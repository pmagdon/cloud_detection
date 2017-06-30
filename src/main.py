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



