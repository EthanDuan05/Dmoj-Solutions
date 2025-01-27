import sys

D = input()
l = int(input())
r = int(input())

L = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
L_2 = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}

K = L[D] - l
K += r

ans = K%4

print(L_2[ans])
