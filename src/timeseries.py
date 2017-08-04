

def extract_timeseries(dic, row, column):
    # extracts the values of the pixel and the dates from the dictionary
    # and puts them as lists in a new dictionary
    values = [value[row, column] for value in dic.values()]
    keys = [key for key in dic.keys()]
    d = {"dates": keys, "values":values}
    return d

