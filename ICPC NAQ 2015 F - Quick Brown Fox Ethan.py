N = int(input())

for i in range(N):
    line = input().split()
    frequency = [0 for _ in range(26)]
    LINE = ''.join(line)
    LINE = LINE.lower()

    for i in LINE:
        if i.isalpha():
            frequency[ord(i)-ord('a')] += 1

    ans = ''
    for i in range(26):
        if frequency[i] == 0:
            ans += chr(ord('a')+i)

    if len(ans) == 0:
        print('pangram')
    else:
        print('missing ' + ans)
