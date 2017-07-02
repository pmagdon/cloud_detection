import pandas as pd
from datetime import datetime



def extract_timeseries(dic, row, column):
    # extracts the values of the pixel and the dates from the dictionary
    # and puts them as lists in a new dictionary
    values = [value[row, column] for value in dic.values()]
    keys = [key for key in dic.keys()]
    d = {"dates": keys, "values":values}
    return d

timeseries = extract_timeseries(dictionary, 0, 0)

df = pd.DataFrame(timeseries, columns = ['dates', 'values']) # creates a dataframe
df.plot(x = "dates", y = "values") # plot time series
