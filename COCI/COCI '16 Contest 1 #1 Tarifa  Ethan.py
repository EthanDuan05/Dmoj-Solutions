max = int(input())
n = int(input())
trans = 0
for i in range(n):
    num = int(input())
    trans = max+trans - num

print(trans+max)