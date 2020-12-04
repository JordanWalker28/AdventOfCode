firstNumber = 0
secondNumber = 0
thirdNumber = 0

def readFile(x):
    numbers = []
    infile = open(x, 'r')
    for line in infile:
        line = line.rstrip("\n")
        numbers.append(str(line))
        
        
    return numbers

def find2NumSum(numbers, target):
    candidates = []
    
    for i, number in enumerate(numbers[:-1]):
        complementary = target - number
        if complementary in numbers[i+1:]:
            candidates.append(number)
            candidates.append(complementary)
            break
        
    return candidates


def find3NumSum(numbers, target):
    candidates = []
    
    for i, number in enumerate(numbers[:-1]):
        for j, number2 in enumerate(numbers[:-1]): 
            complementary = target - number - number2
            if complementary in numbers[i+1:]:
                candidates.append(number)
                candidates.append(complementary)
                candidates.append(number2)
                break
            
    return Remove(candidates)

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

def multList(myList):
    value = 1
    for i in myList:
        value = i * value

    return value
