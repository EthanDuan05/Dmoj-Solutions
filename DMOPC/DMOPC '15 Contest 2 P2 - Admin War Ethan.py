n = int(input())
card_x = input().split()
card_f = input().split()

score_x = 0
score_f = 0

for i in range(n):
    if int(card_x[i]) > int(card_f[i]):
        score_x += 1
    elif int(card_x[i]) < int(card_f[i]):
        score_f += 1
    else:
        continue

print(score_x, score_f)
if score_x > score_f:
    print('Xyene')
elif score_f > score_x:
    print('FatalEagle')
else:
    print('Tie')