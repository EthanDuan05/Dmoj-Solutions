a, b = map(int, input().split())
c, d = map(int, input().split())

sss = [0]*4

s1 = a/c + b/d
s2 = c/d + a/b
s3 = d/b + c/a
s4 = b/a + d/c

sss[0] += s1
sss[1] += s2
sss[2] += s3
sss[3] += s4

cnt = s1
num = 0
for i in range(4):
    if sss[i] > cnt:
        cnt = sss[i]
        num = i

print(num)