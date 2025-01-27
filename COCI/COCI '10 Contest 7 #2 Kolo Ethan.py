import sys

N, K = map(int, input().split())
Letters = ['?' for _ in range(N)]
x = 0

for i in range(K):
    t, l = input().split()
    t = int(t)
    while t > 0:
        t -= 1
        x += 1
        if x == N:
            x = 0
    if Letters[x] != '?' and Letters[x] != l:
        print('!')
        sys.exit(0)
    Letters[x] = l
    # print(x)

for i in range(N):
    for j in range(i+1, N):
        if Letters[i] == Letters[j] and Letters[i] != '?':
            print("!")
            sys.exit(0)

for i in range(N):
    print(Letters[x], end='')
    x -= 1
    if x == -1:
        x = N-1
