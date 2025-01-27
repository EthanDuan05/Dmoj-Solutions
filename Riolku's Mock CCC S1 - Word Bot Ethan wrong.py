N, C, V = map(int, input().split())
word = input()
debug = True

vowel = 'aeiouy'
consonant = 'bcdfghjklmnpqrstvwxyz'
symbol = '*'

cnt_c = 0
cnt_v = 0

last = ''
string_v = ''
string_c = ''
flag = ''

for i in range(N):
    if i == 0:
        last = word[i]
        if word[i] in vowel:
            string_v += word[i]

        if word[i] in consonant:
            string_c += word[i]
        continue

    if last in vowel:
        if word[i] in vowel:
            string_v += word[i]
        else:
            string_c += word[i]
            if len(string_v) > cnt_v:
                cnt_v = len(string_v)
                string_v = ''
                last = word[i]
            else:
                string_v = ''
                last = word[i]

    if last in consonant:
        if word[i] in consonant:
            string_c += word[i]
        else:
            string_v += word[i]
            if len(string_c) > cnt_c:
                cnt_c = len(string_c)
                string_c = ''
                last = word[i]
            else:
                string_c = ''
                last = word[i]

    if i == N-1:
        if len(string_v) > cnt_v:
            cnt_v = len(string_v)

        if len(string_c) > cnt_c:
            cnt_c = len(string_c)

    if debug:
        if len(string_v) > 0:
            print(string_v, 'v')

        if len(string_c) > 0:
            print(string_c, 'c')

if (cnt_v > V) or (cnt_c > C):
    print('NO')
else:
    print('YES')

if debug:
    print(cnt_c, "C")
    print(cnt_v, "V")

