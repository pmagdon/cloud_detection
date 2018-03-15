

def extract_timeseries(dic, band, row, column):
    """
    Extract the time-series for a given pixel and put it in a dictionary.

    Extract the values and the dates of the selected pixel and band from a dictionary storing the values and the dates of
    the image and put them as lists in a new dictionary.

    :param object dic: The dictionary with the dates and the pixel values of the image as arrays.
    :param str band: The band from which the pixel values are extracted.
    :param int row: The row of the pixel.
    :param int column: The column of the pixel.
    :return: A dictionary of length 2, the first item is a list of the dates, the second item is a list of the values.
    """
    keys = [key for key in dic[band].keys()]
    values = [value[row, column] for value in dic[band].values()]
    d = {"dates": keys, "values": values}
    return d
