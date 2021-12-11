from functions import *

BingoCalls = readFileAsSingle('input/day4-1input.txt')
Boards = readFileAsSingleSplit('input/day4-1boards.txt')

print(FindBoard(BingoCalls,Boards,True))
print(FindBoard(BingoCalls,Boards,False))
