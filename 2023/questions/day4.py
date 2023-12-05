import sys
sys.path.append('../functions')
from commonFunctions import *

def calculate(file_path):
    file = read_file(file_path)
    score = 0 
    cards = {} 

    for i, line in enumerate(file):
        cards[i] = cards.get(i, 0) + 1
        card_info = line.split('|') 
        numbers_before = [int(num) for num in card_info[0].split(':')[1].strip().split()] 
        numbers_after = [int(num) for num in card_info[1].strip().split()]
        common_numbers = set(numbers_before).intersection(set(numbers_after))

        val = len(set(numbers_before) & set(numbers_after))
        if len(common_numbers) >= 1:
            score += 2 ** (len(common_numbers) - 1)

        for j in range(val):
            cards[i + 1 + j] = cards.get(i + 1 + j, 0) + cards[i]

    print(score)
    print(sum(cards.values()))

if __name__ == "__main__":
    file_path = setup_file_path('input', 'day4.txt')

    result = calculate(file_path)
