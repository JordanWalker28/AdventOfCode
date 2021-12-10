from functions import *
 
positions = readTextFile('input/day2-1.txt')

answerOne = workoutPositionOne(positions)
answerTwo = workoutPositionTwo(positions)

print(answerOne)
print(answerTwo)

