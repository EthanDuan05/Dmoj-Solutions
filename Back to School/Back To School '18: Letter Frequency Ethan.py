import sys
input = sys.stdin.readline
sentence = input()
psa = []
for k in range(26):
    psa.append([0] * (len(sentence) + 1))

for i in range(len(sentence)):
    character = sentence[i]
    if 'a' <= character <= 'z':
        idx = ord(character) - ord('a')
        for j in range(26):
            if idx == j:
                psa[j][i+1] = psa[j][i] + 1
            else:
                psa[j][i + 1] = psa[j][i] + 0
    else:
        for j in range(26):
            psa[j][i + 1] = psa[j][i] + 0

q = int(input())
for m in range(q):
    a, b, letter = input().split()
    a = int(a)
    b = int(b)
    idx = ord(letter) - ord('a')
    ans = psa[idx][b] - psa[idx][a-1]
    print(ans)