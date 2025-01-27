frequency = [0]*10
n = int(input())
line = list(map(int, input().split()))

for i in range(n):
    frequency[line[i] - 1] += 1

max_ = max(frequency)

for i in range(10):
    if frequency[i] == max_:
        print(i+1)
        break
