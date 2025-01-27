N = int(input())
SCORE = []
FREQUENCT = {}

for i in range(N):
    num = int(input())
    if num not in SCORE:
        SCORE.append(num)

    if num not in FREQUENCT:
        FREQUENCT[num] = 1
    else:
        FREQUENCT[num] += 1

SCORE.sort()
SCORE.reverse()
print(SCORE[2], FREQUENCT[SCORE[2]])