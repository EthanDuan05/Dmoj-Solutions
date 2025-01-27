pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
T = int(input())

combinations = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            for m in range(10):
                if pink*i + green*j + red*k + orange*m == T:
                    if (i, j, k, m) not in combinations:
                        combinations.append((i, j, k, m))

min_sum = 1000000000000000000
for i in combinations:
    print('# of PINK is', i[0], '# of GREEN is', i[1], '# of RED is', i[2], '# of ORANGE is', i[3])
    total = sum(i)
    if total < min_sum:
        min_sum = total

print('Total combinations is '+str(len(combinations))+'.')
print('Minimum number of tickets to print is '+str(min_sum)+'.')