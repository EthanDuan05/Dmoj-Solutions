c = int(input())
cnt = 0
L = []
for i in range(c):
    L.append(input())
for i in range(c):
    answer = input()
    if answer == L[i]:
        cnt += 1
print(cnt)