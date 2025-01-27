n = int(input())

soldier_l = []
for i in range(n):
    soldier = int(input())
    soldier_l.append(soldier)

ans = []
for i in range(n):
    if i == 0:
        if soldier_l[i] <= 41 and soldier_l[i+1] <= 41:
            ans.append(i+1)
    elif 0 < i < n-1:
        if (soldier_l[i] <= 41 and soldier_l[i-1] <= 41) and (soldier_l[i] <= 41 and soldier_l[i+1] <= 41):
            ans.append(i+1)
    else:
        if soldier_l[i] <= 41 and soldier_l[i - 1] <= 41:
            ans.append(i+1)

print(len(ans))