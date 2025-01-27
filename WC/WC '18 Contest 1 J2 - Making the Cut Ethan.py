name = input()
N = []
for i in range(5):
    N.append(input())

if name in N:
    print('Y')
else:
    print('N')