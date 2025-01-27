N = int(input())

for _ in range(N):
    line = input()
    if ' ' in line:
        c = line.find(' ')
        print(c + 1)
    else:
        print(0)
