a, b, c = map(str, input().split('-'))
a = list(a)
b = list(b)
c = list(c)

sum_a = 0
sum_b = 0
sum_c = 0

for i in a:
    sum_a += int(i)

for i in b:
    sum_b += int(i)

for i in c:
    sum_c += int(i)

if sum_a == sum_b == sum_c:
    print('Goony!')
else:
    print('Pick up the phone!')