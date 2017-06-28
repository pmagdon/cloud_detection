def extract_timeseries(dic, row, column):
    print([value[row, column] for value in dic.values()])

extract_timeseries(dictionary, 1,2)
# next step loop
# associate with its key for the x axis of the plot


for item in dictionary.values():
    print(item[0,0])


plt.plot([x], 'o')


x = np.matrix("1 2 3; 4 5 6")
y = np.matrix("7 8 9; 10 11 12")

d = {"a" : x, "b": y}

[value[0,1] for value in d.values()]

for x in range(0,2):
    for y in range(0,3):
        print(x,y)