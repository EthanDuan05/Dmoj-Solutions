N = int(input())

code = [[] for _ in range(5)]

dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

for i in range(5):
    line = list(input().split())
    code[i] = line

for _ in range(N):
    ans = ''
    line = list(input())
    while line:
        first = line.pop(0)
        if first in dic:
            s = int(line.pop(0)) - 1
            f = dic.get(first)
            letter = code[f][s]
            ans += letter
        else:
            ans += first

    print(ans)
