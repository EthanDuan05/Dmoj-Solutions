sum = 0
n = int(input())
for i in range(n):
    line = input()
    for s in range(len(line)):
        if line[s] == 'A':
            sum += 4
        elif line[s] == 'K':
            sum += 3
        elif line[s] == 'Q':
            sum += 2
        elif line[s] == 'J':
            sum += 1
        else:
            sum += 0
print(sum)