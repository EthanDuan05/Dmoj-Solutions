vowel = ['a', 'e', 'i', 'o', 'u']

line = input().split()

ans = []
for i in line:
    if len(i) > 1:
        V = 0
        C = 0
        for s in i:
            if s in vowel:
                V += 1
            else:
                C += 1
        if abs(V - C) <= 1:
            ans.append(True)
        else:
            ans.append(False)
    else:
        if i in vowel:
            ans.append(True)
        else:
            ans.append(False)

if False in ans:
    print('not readable')
else:
    print('readable')