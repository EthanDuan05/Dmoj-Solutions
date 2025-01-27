import sys


def check_pal(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False


W = input()
Pal = []
if len(W) == 1:
    print(1)
    sys.exit(0)

for i in range(len(W)):
    for j in range(i+1, len(W)):
        if check_pal(W[i:j+1]):
            Pal.append(j+1 - i)

print(max(Pal))