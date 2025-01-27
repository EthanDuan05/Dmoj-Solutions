l_1 = input()
l_2 = input()

f1 = [0]*26
f2 = [0]*26

for cha in l_1:
    if cha == ' ':
        continue
    i = ord(cha) - ord('A')
    f1[i] += 1

for cha in l_2:
    if cha == ' ':
        continue
    i = ord(cha) - ord('A')
    f2[i] += 1

if f1 == f2:
    print('Is an anagram.')
else:
    print('Is not an anagram.')