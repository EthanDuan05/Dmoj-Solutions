N = int(input())

X, Y = map(int, input().split())

clap = 0
cnt = 0
flag = True

while flag:
    if X >= 0 and clap < N:
        clap += 2*X
        X -= Y
        cnt += 1
    else:
        if X < 0:
            clap += 0
            cnt += 1
            flag = False

        if clap >= N:
            flag = False


if clap < N:
    print("RIP")
else:
    print(cnt)