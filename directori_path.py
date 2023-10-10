import glob

file_list = glob.glob("./**/*.py",recursive = True)
print(file_list)
print("Total",len(file_list),"files found")
