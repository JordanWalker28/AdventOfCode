import os

def createFolders(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    else:
        print("year already exists")

def createFiles(path, fileType):
    for x in range(1,26):
        fileName = path + '/' + 'day' + str(x) + fileType
        FILE = open(fileName,"w").close()

path = os.getcwd()
print(path)
year = input("Create a folder for year: ")
print(year)

newpath = path + '/' + year
createFolders(newpath)
createFiles(newpath, ".py")

newpath = newpath + '/input'
createFolders(newpath)
createFiles(newpath, ".txt")


