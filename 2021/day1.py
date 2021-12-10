from functions import *
 
numbers = readFile('input/day1-1.txt')

slidingImage = slidingWindow(numbers, 3)
increases = countIncreases(numbers)
newIncreases = countIncreases(slidingImage)
        
print(increases)
print(newIncreases)


