import matplotlib.pyplot as plt
import numpy as np

#def
#    [item[i,j] for item in dictionary.values()]

dictionary["2015-05-15"][0,0]
dictionary["2015-05-10"][0,0]

x = [item[0,0] for item in dictionary.values()]

d = {'numeros': ['1', '2', '3', '4'], 'letras': ['a', 'b', 'c', 'd']}

for item in dictionary.values():
    print(item[0,0])

plt.plot([x], 'o')


x = np.matrix("1 2 3; 4 5 6")
y = np.matrix("7 8 9; 10 11 12")

d = {"a" : x, "b": y}

 [value[0] for value in d.values()]

for x in range(0,2):
    for y in range(0,3):
        print(x,y)