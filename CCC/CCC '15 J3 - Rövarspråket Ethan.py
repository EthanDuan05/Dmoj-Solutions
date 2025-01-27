string = input().strip()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r',
             's', 't', 'v', 'w', 'x', 'y', 'z']

ans = ''
for i in string:
    if i in consonant:
        ans += i

        A = [abs(ord(i) - ord('a')), 'a']
        E = [abs(ord(i) - ord('e')), 'e']
        I = [abs(ord(i) - ord('i')), 'i']
        O = [abs(ord(i) - ord('o')), 'o']
        U = [abs(ord(i) - ord('u')), 'u']

        final = min(A[0], E[0], I[0], O[0], U[0])

        L = [A, E, I, O, U]
        ANS = []
        for s, cha in L:
            if s == final:
                ans += cha
                break

        ind_b = consonant.index(i)
        if i != 'z':
            ans += consonant[ind_b+1]
        else:
            ans += 'z'

    else:
        ans += i


print(ans)
