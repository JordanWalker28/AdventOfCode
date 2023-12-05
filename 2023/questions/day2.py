import sys
sys.path.append('../functions')
from commonFunctions import *
index = {'red': 12, 'blue': 14, 'green': 13}

def calculate_total_sum1(file_path):
    index_count = 0
    sum_of_max = 0
    with open(file_path, 'r') as file:
        for line in file:
            result = True
            game_info = line.split(": ")
            game_name = game_info[0]
            game_data = game_info[1].strip()
            game_rounds = game_data.split(";")
            max_color = {'red': 1, 'blue': 1, 'green': 1}
            for game in game_rounds:
                game_dict = {color: int(quantity) for quantity, color in (item.split() for item in game.split(', '))}
                for color in game_dict:
                    if(game_dict[color] > max_color[color]):
                        max_color[color] = game_dict[color]                        
                    if(game_dict[color] > index[color]):
                        result = False
            start = 1
            for color in max_color:
                start = start * max_color[color]
            sum_of_max += start
                
            if(result is True):
                game_name = game_name.split(" ")
                index_count += int(game_name[1])
    print(sum_of_max)
    return index_count

if __name__ == "__main__":
    file_path = setup_file_path('input', 'day2.txt')

    result = calculate_total_sum1(file_path)
    print (result)
