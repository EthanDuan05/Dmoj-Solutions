n = int(input())
line = list(map(int, input().split()))

sum_left = 0
sum_right = sum(line)

state = False
index = 0
for i in range(n):
    sum_left += line[i]
    sum_right -= line[i]

    if sum_left == sum_right:
        state = True
        index = i+1
        break

if state:
    print(index)
else:
    print('Andrew is sad.')