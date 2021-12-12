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
    
def createDataShape(lines):
    data = [int(line, base=2) for line in lines]
    return data

def createBits(lines):
    bits = [2 ** n for n in range(len(lines[0].strip()))]
    return bits

def calculateEpsilonTimesGamma(data, bits):
    gamma = sum(bit for bit in bits if sum(datum & bit for datum in data) // bit >= len(data) / 2)
    epsilon = sum(bit for bit in bits if sum(datum & bit for datum in data) // bit <= len(data) / 2)
    return epsilon * gamma

def calculateLifeSupport(data, bits):
    filtered_by_most_common = filter_data_bitwise(data, bits)
    filtered_by_least_common = filter_data_bitwise(data, bits, filter_by_most_common=False)
    return filtered_by_most_common[0] * filtered_by_least_common[0]

def filter_data_bitwise(data, bits, filter_by_most_common=True):
    filtered = [x for x in data]
    for bit in reversed(bits):
        ratio = sum(1 for num in filtered if num & bit) / len(filtered)
        wanted_bit_value = bit * int((ratio >= 0.5) == filter_by_most_common)
        filtered = [x for x in filtered if x & bit == wanted_bit_value]
        if len(filtered) == 1:
            break
    return filtered

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
    
def createBoard(Boards):
    boards = []
    for board in Boards:
        rows = [[int(i) for i in row.split()] for row in board.split('\n')]
        boards.append([set(row) for row in rows])
        boards.append([set(col) for col in zip(*rows)])
    return boards

def FindBoard(BingoCalls, Boards, part1):
    BingoCalls = map(int, BingoCalls.split(','))
    Boards = createBoard(Boards)
    for num in BingoCalls:
        for x, board in enumerate(Boards):
                if(part1):
                    if {num} in board:
                        return (sum(sum(group) for group in board) - num) * num
                    else:
                        Boards[x] = [group.difference({num}) for group in board]
                else:
                    if board is not None:
                        if {num} in board:
                            winner = (sum(sum(group) for group in board) - num) * num
                            Boards[x] = None
                            if x % 2:
                                Boards[x-1] = None
                            else:
                                Boards[x+1] = None
                        else:
                            Boards[x] = [group.difference({num}) for group in board]
    return winner
    
