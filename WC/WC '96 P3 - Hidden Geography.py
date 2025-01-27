province_l = {'britishcolumbia': 'a', 'alberta': 'b', 'saskatchewan': 'c',
              'manitoba': 'd', 'ontario': 'e', 'quebec': 'f', 'novascotia': 'g',
              'newfoundland': 'h', 'newbrunswick': 'i', 'pei': 'j'}

full_province = {'a': 'British Columbia', 'b': 'Alberta', 'c': 'Saskatchewan',
                 'd': 'Manitoba', 'e': 'Ontario', 'f': 'Quebec', 'g': 'Nova Scotia',
                 'h': 'Newfoundland', 'i': 'New Brunswick', 'j': 'PEI'}


abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
       'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
       'y', 'z']


ANS = []
for i in range(5):
    ans = ''
    line = input()
    M = line.lower()
    for s in M:
        if s in abc:
            ans += s

    flag = False
    a = ''
    for k in province_l:
        if k in ans:
            a = province_l[k]
            flag = True

    if flag:
        ANS.append(a)
    else:
        ANS.append('*')

for i in ANS:
    if i != '*':
        print(full_province[i])
    else:
        print('NO PROVINCE FOUND')