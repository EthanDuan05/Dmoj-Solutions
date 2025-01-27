L = []
for i in range(3):
    side = int(input())
    L.append(side)

L.sort()

if L[0] + L[1] > L[2]:
    print('Huh? A triangle?')
else:
    print('Maybe I should go out to sea...')