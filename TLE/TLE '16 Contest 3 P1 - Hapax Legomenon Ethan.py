N = int(input())
L = []
distinct = []

for i in range(N):
    word = input()
    L.append(word)

for i in L:
    M = L.count(i)
    if M == 1:
        if i not in distinct:
            distinct.append(i)

print(len(distinct))