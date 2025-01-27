import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))

sum = [0 for _ in range(N + 1)]

sum[0] = 0
sum[1] = 0

for i in range(2, N + 1):
    ans = []
    for k in range(0, N + 1 - i):
        string = line[k: k + i]
        if len(string) == i:
            # print(string)
            state = 0
            while string:
                if len(string) > 1:
                    a = string.pop(0)
                    b = string.pop(-1)
                    state += abs(a - b)
                else:
                    string.clear()
                    state += 0
            ans.append(state)
    sum[i] = min(ans)

for i in range(1, N + 1):
    print(sum[i], end=' ')
