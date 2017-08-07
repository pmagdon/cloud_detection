

def extract_timeseries(dic, row, column):
    # extracts the values and the dates of the selected pixel  from dictionary
    # puts them as lists in a new dictionary
    values = [value[row, column] for value in dic.values()]
    keys = [key for key in dic.keys()]
    d = {"dates": keys, "values": values}
    return d