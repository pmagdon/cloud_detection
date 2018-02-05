import numpy as np

######## Search function example ###########

test_dic = {"date0": np.matrix([[0,0],[np.nan, np.nan]]), "date1": np.full((3, 3), 1, int),
            "date2":  np.full((3, 3), np.nan), "date3": np.full((3,3), 3, int), "date4": np.matrix([[np.nan,2],[3,4]])}

#for date in dictionary_blue_red["blue"].keys():
#    print(date + str(": ") + str(np.mean(dictionary_blue_red["blue"][date])))


################# only test 1 ############################

def only_test1(date, dic_values, dic_mask, par1):
    nrow = dic_values["blue"][date].shape[0]
    ncol = dic_values["blue"][date].shape[1]

    cloud_mask_list = []

    for r in range(0, nrow):
        for c in range(0, ncol):
            cloud_mask_list.append(mtcd_test1(date, r, c, dic_values, dic_mask, par1))

    cloud_mask_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)

    dic_mask.update({date: cloud_mask_array})

    print("Dictionary masked of date %s updated"%(date))

for date in list(dictionary_blue_red["blue"].keys())[1:]:
    only_test1(date, dictionary_blue_red, dictionary_masked, 3)

################# only test 3 #######################


def only_test3(date, dic_values, dic_mask, window_size, cor_coeff):
    nrow = dic_values["blue"][date].shape[0]
    ncol = dic_values["blue"][date].shape[1]

    cloud_mask_list = []

    for r in range(0, nrow):
        for c in range(0, ncol):
            cloud_mask_list.append(mtcd_test3(date, r, c, dic_values, dic_mask, window_size, cor_coeff))

    cloud_mask_array = np.asarray(cloud_mask_list).reshape(nrow, ncol)

    dic_mask.update({date: cloud_mask_array})

    print("Dictionary masked of date %s updated"%(date))

for date in list(dictionary_blue_red["blue"].keys())[1:]:
    only_test3(date, dictionary_blue_red, dictionary_masked, 7, 0.55)
