import sys
input = sys.stdin.readline
line = input()
word = input()

ind = -1
for i in range(len(line)):
    n = len(word)
    if line[i] == word[0]:
        if line[i:n+i] == word:
            ind = i
            break
        else:
            continue

if ind == -1:
    print(-1)
else:
    print(ind)