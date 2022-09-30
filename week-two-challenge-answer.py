# create a folder call inputs
# create a folder called reports
# create a folder called results

# on a regular basis scan the inputs folder and if there are files there check what type of file it is
# xls, xlsx, and html files go to reports
# csv, txt, json files go to results
# any other files types can be deleted



# list the files that are in the inputs folder
import os

current_dir = os.getcwd()
input_dir = current_dir + '\\inputs'

files = os.listdir(input_dir)
print(files)


for file in files:
    # work out the file extension
    extension = file.split(".")[-1]
    print(extension)

    # move the files to the folder based on the extension
    if extension in ['csv', 'txt', 'json']:
        os.rename(input_dir + '\\' + file, current_dir + '\\results\\' + file)
    elif extension in ['xls', 'xlsx', 'html']:
        os.rename(input_dir + '\\' + file, current_dir + '\\reports\\' + file)
    else:
        os.remove(input_dir + '\\' + file)