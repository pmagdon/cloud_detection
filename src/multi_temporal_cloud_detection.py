def mtcd(dataframe):

    refl_blue_dayD = dataframe["values"][0] # extracts the pixel value of an image
    refl_blue_dayref = dataframe["values"][1] # extracts the pixel value of the reference image
    dayD = datetime.strptime(dataframe["dates"][0], "%Y-%m-%d") # extracts the date value
    dayref = datetime.strptime(dataframe["dates"][1], "%Y-%m-%d")

    refl_blue_dayD - refl_blue_dayref > 0.03*(1+(dayD - dayref).total_seconds()/(60*60*24)/30) # test blue band


