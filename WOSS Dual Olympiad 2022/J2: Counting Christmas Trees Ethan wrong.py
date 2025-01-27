N = int(input())

line = list(map(int, input().split()))

max_increase = 0
max_decrease = 0

increase = []
decrease = []

for i in range(N):
    if i < N-1:
        first = line[i]
        second = line[i+1]
        if first < second:
            if len(decrease) >= max_decrease:
                max_decrease = len(decrease)
                decrease = []
            else:
                decrease = []

            if first not in increase:
                increase.append(first)
            if second not in increase:
                increase.append(second)

        elif first > second:
            if len(increase) >= max_increase:
                max_increase = len(increase)
                increase = []
            else:
                increase = []

            if first not in decrease:
                decrease.append(first)
            if second not in decrease:
                decrease.append(second)

    else:
        if len(decrease) >= max_decrease:
            max_decrease = len(decrease)

        if len(increase) >= max_increase:
            max_increase = len(increase)

print(max_increase)
print(max_decrease)
