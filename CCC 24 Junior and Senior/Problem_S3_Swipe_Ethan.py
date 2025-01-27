N = int(input())
A = input()
B = input()

A_O = [0 for _ in range(N)]
B_O = [0 for _ in range(N)]
different = 0
D_position = []

for i in range(N):
    if A[i] != B[i]:
        A_O[i] = 0
        B_O[i] = 0
        different += 1
        D_position.append(i)
    else:
        A_O[i] = 1
        B_O[i] = 1

if different == 0:
    print('YES')
    print(0)

'''
if N == 2:
    if len(D_position) == 1:
        if D_position[0] == N-1:
'''
