

def extract_timeseries(dic, band, row, column):
    # extract the values and the dates of the selected pixel and band from dictionary
    # put them as lists in a new dictionary
    keys = [key for key in dic[band].keys()]
    values = [value[row, column] for value in dic[band].values()]
    d = {"dates": keys, "values": values}
    return d
