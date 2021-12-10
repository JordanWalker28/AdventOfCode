def readFile(x):
    with open(x, 'r') as f:
        lines = f.readlines()
    input = [int(entry.strip()) for entry in lines]
    return input
    
def countIncreases(list):
    newIncreases = 0
    for x in range (1 , len(list)):
        if list[x] > list[x - 1]:
            newIncreases += 1
    return newIncreases
    
def slidingWindow(list, windowSize):
    slidingImage = []
    currentItem = 0
    for i in range(len(list) - windowSize + 1):
        currentItem = sum(list[i: i + windowSize])
        slidingImage.append(currentItem)
    return slidingImage
    
