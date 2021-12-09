def readFile(x):
    with open(x, 'r') as f:
        lines = f.readlines()
    input = [int(entry.strip()) for entry in lines]
    return input
    
