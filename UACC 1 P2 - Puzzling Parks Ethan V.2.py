import sys
input = sys.stdin.readline

'''
when N is an even number:
N:     Steps:
2      1
4      5 (plus 4)
6      7 (plus 2)
8      11 (plus 4)
10     13 (plus 2)
12     17 (plus 4)

when N is an odd number:
N:     Steps:
3      4
5      6 (plus 2)
7      10 (plus 4)
9      12 (plus 2)
11     16 (plus 4)

'''
N = int(input())
ANS = 0
if N % 2 == 0:
    ans = 1
    add = (N-2) // 4
    ans += add * 6
    if N % 4 == 0:
        ans += 4

    ANS = ans

elif N % 2 == 1:
    ans = 4
    add = (N-3) // 4
    ans += add * 6
    if (N - 3) % 4 == 2:
        ans += 2

    ANS = ans

print(ANS)