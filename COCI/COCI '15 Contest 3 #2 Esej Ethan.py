import random

A, B = map(int, input().split())

S = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
     'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'x', 'z']

N = [1, 2, 3, 4, 5, 6, 7]
ANS = []

while B > 0:
    phrase = ''
    for _ in range(random.choice(N)):
        phrase += random.choice(S)
    ANS.append(phrase)
    B -= 1

print(' '.join(ANS))
