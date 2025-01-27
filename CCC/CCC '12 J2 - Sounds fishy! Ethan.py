L = []
for i in range(4):
    N = int(input())
    L.append(N)

if L[0] < L[1] < L[2] < L[3]:
    print('Fish Rising')
elif L[0] > L[1] > L[2] > L[3]:
    print('Fish Diving')
elif L[0] == L[1] == L[2] == L[3]:
    print('Fish At Constant Depth')
else:
    print('No Fish')