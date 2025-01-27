n = int(input())
name = ''
score = -1

for i in range(n):
    s, num = input().split()
    num = float(num)
    if num > score:
        name = s
        score = num

print(name)