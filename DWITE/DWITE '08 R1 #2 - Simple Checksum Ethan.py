refer = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
         'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
         'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
         'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
         'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
         'Z': 26}

ANS = []
for _ in range(5):
    line, match = input().split()
    line = list(line)
    total = 0
    for s in range(6):
        total += int(line[s])
    total = str(total)
    ans = 0
    for l in total:
        ans += int(l)
    if ans == refer[match]:
        ANS.append('match')
    else:
        ANS.append('error')

for i in ANS:
    print(i)