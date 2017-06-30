import numpy as np
from timeseries import extract_timeseries
x = np.matrix("1 2 3; 4 5 6")
y = np.matrix("7 8 9; 10 11 12")

d = {"a" : x, "b": y}


def extract_timeseries(dic):
    for x in range(0,2):
        for y in range(0,3):
            print([value[x, y] for value in dic.values()])

length_dict = {a: len(value) for a, value in d.items()}

np.empty(2,3,2)

 [value[0,0] for value in d.values()]

for x in range(0,2):
    for y in range(0,3):
        print(x,y)

for x in range(0,2):
    for y in range(0,3):
        print([value[x, y] for value in d.values()])


values = list(zip(*d.values())) # gives [([1, 2, 3], [7, 8, 9]), ([4, 5, 6], [10, 11, 12])]
pairs = []
for value in values:
    pairs.extend(list(zip(*value))) #adds (1, 7), (2, 8), ... to pairs list

for pair in pairs:
    print(pair)

def currency_converter(rate, euros):
    dollars=euros*rate
    return dollars

x = currency_converter(100, 1000)