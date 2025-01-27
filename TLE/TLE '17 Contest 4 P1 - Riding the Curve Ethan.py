M, K, N = map(int, input().split())

flag = True
for i in range(0, M+1):
    if (i + K) / N >= 0.595:
        print(i)
        flag = False
        break

if flag:
    print('have mercy snew')