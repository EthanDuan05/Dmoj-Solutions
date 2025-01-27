Vowel = ['a', 'e', 'i', 'o', 'u']

for _ in range(5):
    w1, w2 = input().split()
    w1_f = [0] * len(w1)
    w2_f = [0] * len(w2)
    for i in range(len(w1)):
        if w1[i] in Vowel:
            w1_f[i] += 1

    for i in range(len(w2)):
        if w2[i] in Vowel:
            w2_f[i] += 1

    if w1_f == w2_f:
        print('same')
    else:
        print('different')
