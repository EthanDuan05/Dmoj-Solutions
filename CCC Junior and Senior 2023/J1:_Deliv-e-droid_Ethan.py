P = int(input())
C = int(input())

score = 50*P - 10*C

if P > C:
    score += 500

print(score)