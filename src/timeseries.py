#
def extract_timeseries(dic, row, column):
    # function not so useful because you have to give manually
    # the number of row and column from which you want the timeseries
    print([value[row, column] for value in dic.values()])


def extract_timeseries(dic):
    # a bit more useful, because the number row and column is integrated,
    # but only specific for this picture size...
    for x in range(0,528):
        for y in range(0,720):
            print([value[x, y] for value in dic.values()])


def extract_timeseries(dic):
    # prints lists of pairs of values with the same position in a dictionary
    # that contains matrix
    row = next(len(i) for i in dic.values()) + 1
    col = next(i.shape[1] for i in dic.values()) + 1
    for x in range(0, row):
        for y in range(0,col):
            print([value[x, y] for value in dic.values()])

def extract_timeseries(dic):
    # the same as the last one, but also prints class
    # and dictionary keys
    row = next(len(i) for i in dic.values()) + 1
    col = next(i.shape[1] for i in dic.values()) + 1
    for x in range(0, row):
        for y in range(0, col):
            print([values[x, y] for values in dic.values()])
            print(type([value[x, y] for value in dic.values()]))
            print(dic.keys())

def extract_timeseries(dic):
    # the same as the last one, but also prints class
    # and dictionary keys
    row = next(len(i) for i in dic.values()) + 1
    col = next(i.shape[1] for i in dic.values()) + 1
    for x in range(0, row):
        for y in range(0, col):
            print([values[x, y] for values in dic.values()])
            #print(type([value[x, y] for value in dic.values()]))
            print(dic.keys())


def get_keys(dic):
    # prints the keys of the dictionary (in this case the date info)
    # for so many times as values in the matrix (in this case pixels)
    row = next(len(i) for i in dic.values()) + 1
    col = next(i.shape[1] for i in dic.values()) + 1
    for i in range(0, row * col + 1):
        print(dic.keys())

# zip(get_keys(dictionary), extract_timeseries(dictionary) )

#########################################################
# next step
# associate with its key for the x axis of the plot
#########################################################

#########################################################
# nice easy dictionary for inspiration
x = np.matrix("1 2 3; 4 5 6")
y = np.matrix("7 8 9; 10 11 12")

d = {"a" : x, "b": y}

def extract_timeseries(dic):
    for x in range(0,2):
        for y in range(0,3):
            print([value[x, y] for value in d.values()])

def get_keys(dic):
    for i in range(0,7):
        print(d.keys())

zip(extract_timeseries(d), get_keys(d))



