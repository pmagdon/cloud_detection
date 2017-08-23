import numpy as np


dictionary_blue_red["blue"]["2015-05-10"][row][col]


def mtcd_test3(row, col, dic):

    up =  row - 1
    down = row + 1
    right = col + 1
    left = col - 1

    date_ref = [key for key in dic.keys()][0]
    date = [key for key in dic.keys()][1]

    a = dic["blue"][date][up,left]
    b = dic["blue"][date][up,col]
    c = dic["blue"][date][up,right]
    d = dic["blue"][date][row,left]
    e = dic["blue"][date][row,col]
    f = dic["blue"][date][row,right]
    g = dic["blue"][date][down,left]
    h = dic["blue"][date][down,col]
    i = dic["blue"][date][down,right]

    aref = dic["blue"][date_ref][up,left]
    bref = dic["blue"][date_ref][up,col]
    cref = dic["blue"][date_ref][up,right]
    dref = dic["blue"][date_ref][row,left]
    eref = dic["blue"][date_ref][row,col]
    fref = dic["blue"][date_ref][row,right]
    gref = dic["blue"][date_ref][down,left]
    hfref = dic["blue"][date_ref][down,col]
    iref = dic["blue"][date_ref][down,right]

    date_neighb = [a, b, c, d, e, f, g, h, i]
    date_ref_neighb = [A, B, C, D, E, F, G, H, I]

list1 = [1, 2, 3]
list2 = [2, 4, 6]
np.corrcoef(list1, list2)