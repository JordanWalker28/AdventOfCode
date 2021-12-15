import os

path = os.getcwd()
print(path)
year = input("Create a folder for year: ")
print(year)

newpath = path + '/' + year
if not os.path.exists(newpath):
    os.makedirs(newpath)
else:
    print("year already exists")
