import os

def calculate_total_sum1(file_path):
    # Open the file
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
    # Define a dictionary to map numeric words to digits
    word_to_digit = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                     'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    # Open the file
    with open(file_path, 'r') as file:
        total_sum = 0

        for line in file:
            first_digit = None
            last_digit = None
            line_sum = 0

            current_word = ''
            for char in line:
                # Check if the character is alphanumeric
                if char.isalnum():
                    # Check if the character is a digit
                    if char.isdigit():
                        if first_digit is None:
                            first_digit = char
                        last_digit = char
                    else:
                        # Construct the current word by appending non-digit characters
                        current_word += char.lower()

                        # Check if the current word is a numeric word
                        if current_word in word_to_digit:
                            digit = word_to_digit[current_word]
                            if first_digit is None:
                                first_digit = digit
                            last_digit = digit
                            current_word = ''

            if first_digit is not None and last_digit is not None:
                line_sum = int(first_digit + last_digit)
                total_sum += line_sum

    return total_sum

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(script_dir)
    relative_path = os.path.join('testInput', 'day1_2.txt')
    file_path = os.path.join(parent_dir, relative_path)

    # result = calculate_total_sum1(file_path)
    # print(result)
    
    result2 = calculate_total_sum2(file_path)
    print(result2)