a, b = input().split()
a = list(a)
a.reverse()
b = list(b)
b.reverse()
ans_a = ''
ans_b = ''

for i in a:
    ans_a += i

for i in b:
    ans_b += i

if int(ans_a) > int(ans_b):
    print(ans_a)
elif int(ans_a) < int(ans_b):
    print(ans_b)