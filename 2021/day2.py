from functions import *
 
positions = readTextFile('input/day2-1.txt')

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
        
print(horizontal * depth)

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

print(horizontal * depth)

