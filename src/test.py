import datetime
from src.timeseries import extract_timeseries
import pandas as pd
import numpy as np
import math

##########################


image = np.arange(100).reshape(10,10)
#image = np.random.randint(0,100,100).reshape(10,10)

def moving_window(dic, date, row, col, size, edge='nan'):
    """ Function to extract the values within an analysis window from an 2d Array
    Args:
        array:  the image from which to extract all the moving windows
        size: the siez of the movong window as odd number
        edge: a string argument to specify how to handle the edges
    Returns:
         None and prints all windows
    """

    if size%2 == 0:
        raise ValueError(" Size needs to be odd!")
    if edge != 'nan':
        raise ValueError(" Edge argument needs to of 'nan', ...")

    sz = math.floor(size / 2)
    #Apply padding with nan add edge
    array = dic["blue"][date]
    array_with_margins = np.pad(array.astype(float),pad_width=sz,mode='constant',constant_values=np.nan)
    result = array_with_margins[row - sz:row + sz + 1, col - sz:col + sz + 1]

    return result


################# Pauls original function ########################

image = np.arange(100).reshape(10,10)
#image = np.random.randint(0,100,100).reshape(10,10)

def moving_window(array, size,edge='nan'):
    """ Function to extract the values within an analysis window from an 2d Array
    Args:
        array:  the image from which to extract all the moving windows
        size: the siez of the movong window as odd number
        edge: a string argument to specify how to handle the edges
    Returns:
         None and prints all windows
    """

    if size%2 == 0:
        raise ValueError(" Size needs to be odd!")
    if edge != 'nan':
        raise ValueError(" Edge argument needs to of 'nan', ...")

    sz = math.floor(size / 2)
    #Apply padding with nan add edge
    array = np.pad(array.astype(float),pad_width=sz,mode='constant',constant_values=np.nan)

    for row in range(sz, array.shape[0]-sz):
        for col in range(sz, image.shape[1]-sz):
            print(array[row-sz:row + sz + 1, col-sz:col+sz+1])


moving_window(image, 3,edge='nan')

