import sys

N, C, V = map(int, input().split())
line = list(input())

vowel = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxyz'

max_c = 0
max_v = 0

flag = True
last = line[0]

if N == 1:
    print('YES')
    sys.exit(0)

if line[0] in vowel:
    max_v += 1

if line[0] in consonants:
    max_c += 1

line.pop(0)

for i in line:
    if last in vowel:
        if i in vowel:
            max_v += 1
            last = i
        else:
            last = i
            max_v = 0

    if last in consonants:
        if i in consonants:
            max_c += 1
            last = i
        else:
            last = i
            max_c = 0

    print(last, max_v)

    if max_c > C:
        flag = False
        break

    if max_v > V:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')

print(max_v)
print(max_c)
