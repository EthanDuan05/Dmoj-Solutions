S1, S2 = input().split(',')
L = []
print(S2)
Marks = ['.', '?', '!']
if S2 in Marks:
    L.append(S1)
    L.append(S2)
    print(''.join(L))
else:
    S2 = S2[1:]
    M = S2[-1]
    S2 = S2[0: -1]

    if S2[0].islower():
        S2 = S2[0].upper() + S2[1:]

    L.append(S2)

    if S1[0].isupper():
        S1 = S1[0].lower() + S1[1:]

    L.append(S1)
    print(' '.join(L) + M)
