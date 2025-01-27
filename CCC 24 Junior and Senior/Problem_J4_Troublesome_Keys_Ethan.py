a = input()
b = input()

# case 1, length are same
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            print(a[i], b[i])
            print('-')

# case 2, different length
else:
    D = []
    S = {}
    Silent_letter = ''
    WRONG_KEY = ''
    frequency_a = [0 for i in range(26)]
    frequency_b = [0 for i in range(26)]

    for i in a:
        frequency_a[ord(i) - ord('a')] += 1

    for j in b:
        frequency_b[ord(j) - ord('a')] += 1

    for i in range(26):
        if frequency_a[i] > frequency_b[i] == 0:
            D.append(frequency_a[i])
            S[frequency_a[i]] = chr(ord('a') + i)

        if frequency_b[i] > frequency_a[i] == 0:
            D.append(frequency_b[i])
            S[frequency_b[i]] = chr(ord('a') + i)

    print(frequency_a)
    print(frequency_b)
    print(D)

    F = [0 for i in range(20)]
    for i in D:
        F[i] += 1

    for i in F:
        if i > 2:
            WRONG_KEY += S[i]

    print(WRONG_KEY)



