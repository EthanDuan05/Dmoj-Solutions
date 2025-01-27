a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

Nikky = 0
Bryon = 0

cnt_n = 0
cnt_b = 0

while True:
    if cnt_n + a < s:
        Nikky += a
        Nikky -= b
        cnt_n += a + b
    if cnt_n + a == s:
        Nikky += a
        cnt_n += a
    elif cnt_n + a > s:
        Nikky += s - cnt_n
        cnt_n += s - cnt_n
        break

while True:
    if cnt_b + c < s:
        Bryon += c
        Bryon -= d
        cnt_b += c + d
    if cnt_b + c == s:
        Bryon += c
        cnt_b += c
    elif cnt_b + c > s:
        Bryon += s - cnt_b
        cnt_b += s - cnt_b
        break

if Bryon > Nikky:
    print('Byron')
elif Nikky > Bryon:
    print('Nikky')
else:
    print('Tied')
