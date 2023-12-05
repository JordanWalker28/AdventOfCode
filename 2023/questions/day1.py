import sys
sys.path.append('../functions')
from commonFunctions import *

def calculate_total_sum1(file_path):
    with open(file_path, 'r') as file:
        total_sum = 0

        for line in file:
            first_digit = None
            last_digit = None
            line_sum = 0

            for char in line:
                if char.isdigit():
                    last_digit = char
                    if first_digit is None:
                        first_digit = char
            
            if first_digit is not None and last_digit is not None:
                line_sum = int(first_digit + last_digit)
                total_sum += line_sum

        return total_sum
    
def calculate_total_sum2(file_path):
    with open(file_path, 'r') as file:
        total_sum = 0

        for line in file:
            line_sum = get_first_and_last_digits(line)
            total_sum += line_sum

        return total_sum

                
def get_first_and_last_digits(line):
    lettermap = {
        letters: str(number + 1)
        for number, letters in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        )
    }

    line_sum = 0
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)

        for letters, number in lettermap.items():
            if line[i:].startswith(letters):
                digits.append(number)

    line_sum += int(digits[0] + digits[-1])
    return line_sum

if __name__ == "__main__":
    file_path = setup_file_path('input', 'day1.txt')

    result = calculate_total_sum1(file_path)
    result2 = calculate_total_sum2(file_path)

    print(result)
    print(result2)
