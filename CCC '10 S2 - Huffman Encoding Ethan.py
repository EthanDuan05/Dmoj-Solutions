N = int(input())
D = {}

for _ in range(N):
    a, b = input().split()
    D[b] = a

line = input()

word = ''
ANS = ''
for i in line:
    word += i
    if word in D.keys():
        ANS += D[word]
        word = ''

print(ANS)