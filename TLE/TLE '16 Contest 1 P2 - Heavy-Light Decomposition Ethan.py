import sys

N = int(input())

Total = 0
M = {}
List = []

if N == 1:
    num = int(input())
    print(num)
    sys.exit(0)

for _ in range(N):
    num = int(input())
    Total += num

    if num not in M:
        M[num] = 1
    else:
        M[num] += 1
    List.append(num)

Mean = Total / N
Mode = max(M.values())
Mode_f = [k for k in M if M[k] == Mode]
if len(Mode_f) > 1:
    Final_Mode = sum(Mode_f) / len(Mode_f)
else:
    Final_Mode = Mode_f[0]
List.sort()

if N % 2 == 0:
    a = List[((N // 2)-1)]
    b = List[(N // 2)]
    Median = (a + b) // 2
else:
    ind = (N+1) // 2
    Median = List[int(ind) - 1]

cnt_Mean = 0
cnt_Mode = 0
cnt_Median = 0
for i in List:
    if i <= Mean:
        cnt_Mean += 1

    if i <= Final_Mode:
        cnt_Mode += 1

    if i <= Median:
        cnt_Median += 1

print(min(cnt_Mean, cnt_Mode, cnt_Median))