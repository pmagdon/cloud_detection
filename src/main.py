import numpy as np
import pandas as pd

#  Run

image_files = [] # create an empty list

# run first_import function before you continue

first_import("data/clip1.tif") # maybe here we can also use a loop and do the first import
                               # for all the images in a folder
first_import("data/clip2.tif")

dictionary_blue = {}
dictionary_red = {}

# run import_image function before you continue

for images in image_files:
    # reads all the image files in the list
    import_image(images, 3, dictionary_blue)   # blue band

for images in image_files:
    # reads all the image files in the list
    import_image(images, 1, dictionary_red)   # red band

# run extract_timeseries function before you continue

timeseries = extract_timeseries(dictionary_blue, 0, 0)

df = pd.DataFrame(timeseries) # creates a dataframe
df.plot(x = "dates", y = "values") # plot time series

# run mtcd function before you continue

row = next(len(i) for i in dictionary_blue.values())
column = next(i.shape[1] for i in dictionary_blue.values())

for row in range(0,row):
    for column in range(0,column):
        print(mtcd(dictionary, row, column))


########################  Test #############################

# 1. Test: for loop to extract time series for all pixel values and put it to a list

timeseries_all = []
for x in range(0, next(len(i) for i in dictionary.values())):
    for y in range(0, next(i.shape[1] for i in dictionary.values())):
        timeseries_all.append(extract_timeseries(dictionary, x, y))

# and now put the values on the lists in dataframes
for x in range(0,len(timeseries_all)):
    pd.DataFrame(timeseries_all[x])


# 2. Test: easy dictionary

x = np.matrix("1 2 3; 4 5 6")
y = np.matrix("7 8 9; 10 11 12")

d = {"a" : x, "b": y}

def timeseries(dic):
    for x in range(0,2):
        for y in range(0,1):
            print([value[x, y] for value in dic.values()])


 [value[0,0] for value in d.values()]


# 3. Test: time series functions that I will not use

def extract_timeseries(dic):
    # a bit more useful, because the number row and column is integrated,
    # but only specific for this picture size...
    for x in range(0,527):
        for y in range(0,719):
            print([value[x, y] for value in dic.values()])


def extract_timeseries(dic):
    # prints lists of pairs of values with the same position in a dictionary
    # that contains matrix. also prints class and dictionary keys
    row = next(len(i) for i in dic.values())
    col = next(i.shape[1] for i in dic.values())
    for x in range(0, row):
        for y in range(0,col):
            print([value[x, y] for value in dic.values()])
            print(type([value[x, y] for value in dic.values()]))
            print(dic.keys())

def get_keys(dic):
    # prints the keys of the dictionary (in this case the date info)
    # for so many times as values in the matrix (in this case pixels)
    row = next(len(i) for i in dic.values())
    col = next(i.shape[1] for i in dic.values())
    for i in range(0, row * col + 1):
        print(dic.keys())


# 4. Test: alte mtcd function: time series defined before and outside of the mtcd function definition
def mtcd(dataframe):

    refl_blue_dayD = dataframe["values"][0] # extracts the pixel value of an image
    refl_blue_dayref = dataframe["values"][1] # extracts the pixel value of the reference image
    dayD = datetime.datetime.strptime(dataframe["dates"][0], "%Y-%m-%d") # extracts the date value
    dayref = datetime.datetime.strptime(dataframe["dates"][1], "%Y-%m-%d")# extracts the data value of the reference image

    refl_red_dayD = data_frame["values"][0]
    refl_red_dayref = data_frame["values"][1]

    if abs(refl_blue_dayD - refl_blue_dayref) > 0.03*(1+abs(dayD - dayref).total_seconds()/(60*60*24)/30) and \
                    abs(refl_red_dayD - refl_red_dayref) > 1.5 * (abs(dayD - dayref).total_seconds() / (60 * 60 * 24)):
        return "change"
    else:
        return "no change"