N = int(input())

for _ in range(N):
    terms = []
    times = []
    line = list(input())
    length = len(line)
    last = line[0]
    current = 1
    for i in range(1, length):
        if line[i] != last:
            print(current, last, end=' ')
            terms.append(last)
            times.append(current)
            last = line[i]
            current = 1
        else:
            current += 1

        if i == length-1:
            print(current, last)
