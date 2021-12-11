def readFile(x):
    with open(x, 'r') as f:
        lines = f.readlines()
        input = [int(entry.strip()) for entry in lines]
    return input
      
def readTextFile(x):
    with open(x, 'r') as f:
        lines = f.readlines()
    return lines
    
def readFileAsSingle(x):
    with open(x, 'r') as f:
            line = f.read()
    return line
    
def readFileAsSingleSplit(x):
    with open(x, 'r') as f:
            line = f.read().split('\n\n')
    return line
 
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

def workoutPositionOne(positions):
    horizontal = 0
    depth = 0
    
    for x in positions:
        a,b = x.split(' ', 1)
        if(a == "forward"):
            horizontal += int(b)
        elif(a == "up"):
            depth -= int(b)
        else:
            depth += int(b)
    return horizontal * depth
    
def workoutPositionTwo(positions):
    horizontal = 0
    depth = 0
    aim = 0

    for x in positions:
        a,b = x.split(' ', 1)
        if(a == "forward"):
            horizontal += int(b)
            if(aim == 0):
                depth += depth * 1
            else:
                depth += aim * int(b)
        elif(a == "up"):
            aim -= int(b)
        else:
            aim += int(b)
    return horizontal * depth
    
