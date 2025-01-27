a, b, c = map(int, input().split())
C = int(input())

flag = True
for i in range(0, 100+1):
    for s in range(0, 100+1):
        for k in range(0, 100+1):
            sum = a*i + b*s + c*k
            if sum == C:
                flag = False
                break

if flag:
    print('TRY AGAIN')
else:
    print('QUEST CLEARED')