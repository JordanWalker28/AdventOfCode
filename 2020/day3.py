from functions import *

numbers = readFile('day3.txt')

def day3(numbers, seq):
    treeCount = 0

    row, col = 0, 0

    while row +1 < len(numbers):
        col+=seq[0]
        row+= seq[1]

        
        space = numbers[row][col % len(numbers[row])]
        
        if space== '#':
            treeCount += 1

    return(treeCount)

print(day3(numbers, (3,1)))

list = [(1,1), (3,1), (5,1), (7,1), (1,2)]

sum = 1

for i in list:
    sum = sum * day3(numbers, i)
    print(sum)
    
print(sum)

