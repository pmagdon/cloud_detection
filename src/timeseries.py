

def extract_timeseries(dic, row, column):
    # extracts the values of the pixel over different years
    # pixel determined by row and column
    return([value[row, column] for value in dic.values()]), (dic.keys()) # this works fine





def extract_timeseries(dic, row, column):
    # extracts the values of the pixel over different years
    # puts the values in a dictionary
    values = ([value[row, column] for value in dic.values()])
    keys = (dic.keys())
    d= {keys: values}
    return d

# unhashable type: 'dict_keys'  --> error when I run this function
# solve this error or try to work with the output of the first function
