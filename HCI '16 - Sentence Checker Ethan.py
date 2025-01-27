N = int(input())
L = []

for _ in range(N):
    word = input()
    L.append(word)

sentence = input().split()

flag = True
for i in sentence:
    if i in L:
        continue
    else:
        flag = False
        break
if flag:
    print('Correct')
else:
    print('Incorrect')