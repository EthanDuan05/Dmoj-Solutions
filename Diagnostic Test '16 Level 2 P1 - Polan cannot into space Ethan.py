flag = True
sum = 0

D = {'one': 1,
     'two': 2,
     'three': 3,
     'four': 4,
     'five': 5,
     'six': 6,
     'seven': 7,
     'eight': 8,
     'nine': 9,
     'zero': 0}

while flag:
    line = input()
    if line == 'No more numbers.':
        flag = False
    else:
        sum += D[line]

print(sum)