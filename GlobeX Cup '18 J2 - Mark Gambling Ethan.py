N = int(input())
line = list(map(int, input().split()))

average = int((sum(line) / N)*10)/10

cnt = 0
for i in range(N):
    if line[i] > average:
        cnt += 1

portion = (cnt / N) * 100
if portion > 50:
    print('Winnie should take the risk')
else:
    print("That's too risky")