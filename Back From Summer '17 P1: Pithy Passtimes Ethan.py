n = int(input())
phrase = input().split()
cnt = 0
for i in range(n):
    if len(phrase[i]) <= 10:
        cnt += 1
print(cnt)
