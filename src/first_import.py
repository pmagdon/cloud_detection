image_files = [] # create an empty list

def first_import(filename):
    # updates a list with the names of the image files
    image_files.append(filename)
    print("File added to list")

first_import("data/clip1.tif")
first_import("data/clip2.tif")

dictionary = {}

for x in image_files: # reads all the image files in the list
    import_image(x, 1, dictionary)