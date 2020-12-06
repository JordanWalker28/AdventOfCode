from functions import *

numbers = readFile('input/day2.txt')

line = []

firstCount = 0
secondCount = 0

for i in numbers:
    counter = 0
    count, letter, text = i.split(" ")
    count = count.split("-")
    letter = letter.rstrip(":")

    first = int(count[0]) -1
    second = int(count[1]) -1
    counter = text.count(letter)
    
    if(counter >= int(count[0]) and counter <= int(count[1])):
        firstCount += 1
        
    if(text[first] == letter and text[second] != letter):
        secondCount += 1
    if(text[first] != letter and text[second] == letter):
        secondCount += 1

print("Part One")
print(firstCount)

print("Part Two")
print(secondCount)



