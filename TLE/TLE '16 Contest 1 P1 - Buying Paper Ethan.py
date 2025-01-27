D = int(input())
Dime = list(map(int, input().split()))
Q = int(input())
Quarter = list(map(int, input().split()))

Dime.sort()
Quarter.sort()

if (Dime[D-1] / 10) < (Quarter[0] / 25):
    print('Dimes are better')
elif (Quarter[Q-1] / 25) < (Dime[0] / 10):
    print('Quarters are better')
else:
    print('Neither coin is better')