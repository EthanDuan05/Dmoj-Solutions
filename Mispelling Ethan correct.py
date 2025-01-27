N = int(input())

for i in range(N):
    line = input()
    space = line.index(' ')
    index = int(line[0:space])
    string = list(line[space+1:])

    if index == 0:
        print(i+1, ''.join(string))
    else:
        string.pop(index-1)
        print(i+1, ''.join(string))