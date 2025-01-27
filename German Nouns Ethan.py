N = int(input())

for _ in range(N):
    cnt = 0
    line = input().split()
    for i in line:
        if i[0].isupper():
            cnt += 1
    print(cnt)