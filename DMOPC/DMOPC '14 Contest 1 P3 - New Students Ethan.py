I = int(input())
total = 0
cnt_student = I
for i in range(I):
    num = int(input())
    total += num

S = int(input())

ANS = []
for i in range(S):
    new = int(input())
    total += new
    cnt_student += 1
    ans = total / cnt_student
    ANS.append('{:.3f}'.format(ans))

for i in ANS:
    print(i)