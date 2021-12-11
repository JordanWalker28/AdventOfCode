from functions import *

def create_boards(num_data, board_data):
    nums = map(int, num_data.split(','))
    boards = []
    for board in board_data:
        rows = [[int(i) for i in row.split()] for row in board.split('\n')]
        boards.append([set(row) for row in rows])
        boards.append([set(col) for col in zip(*rows)])
    return nums, boards

def GetWinningScore(num, board):
    return (sum(sum(group) for group in board) - num) * num

def FindWinningBoard(num_data,board_data):
    nums, boards = create_boards(num_data, board_data)
    for num in nums:
        for idx, board in enumerate(boards):
            if {num} in board:
                return GetWinningScore(num, board)
            else:
                boards[idx] = [group.difference({num}) for group in board]

def FindLastWinningBoard(num_data,board_data):
    nums, boards = create_boards(num_data, board_data)
    for num in nums:
        for idx, board in enumerate(boards):
            if board is not None:
                if {num} in board:
                    winner = GetWinningScore(num, board)
                    boards[idx] = None
                    if idx % 2:
                        boards[idx-1] = None
                    else:
                        boards[idx+1] = None
                else:
                    boards[idx] = [group.difference({num}) for group in board]
    return winner


BingoCalls = readFileAsSingle('input/day4-1input.txt')
Boards = readFileAsSingleSplit('input/day4-1boards.txt')


    
print(FindWinningBoard(BingoCalls,Boards ))
print(FindLastWinningBoard(BingoCalls,Boards ))
