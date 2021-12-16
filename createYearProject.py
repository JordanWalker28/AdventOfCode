import os

def createFolders(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    else:
        print("year already exists")

path = os.getcwd()
print(path)
year = input("Create a folder for year: ")
print(year)

newpath = path + '/' + year
createFolders(newpath)

for x in range(1,26):
    fileName = newpath + '/' + 'day' + str(x) + '.py'
    FILE = open(fileName,"w").close()

newpath = newpath + '/input'
createFolders(newpath)



