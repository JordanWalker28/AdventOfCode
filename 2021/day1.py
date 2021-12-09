
from functions import *

numbers = readFile('input/day1-1.txt')

increases = 0
for x in range (1 , len(numbers)):
    if numbers[x] > numbers[x - 1]:
        increases += 1
        
print(increases)
