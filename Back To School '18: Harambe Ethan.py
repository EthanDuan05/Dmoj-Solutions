import sys

line1 = input()
line2 = input()
K = int(input())

changed = 0
for i in range(len(line1)):
    if line1[i] != line2[i]:
        if (line1[i] == ' ' and line2[i] != ' ') or (line1[i] != ' ' and line2[i] == ' '):
            print('No plagiarism')
            sys.exit(0)
        else:
            changed += 1

if changed <= K:
    print('Plagiarized')
else:
    print('No plagiarism')