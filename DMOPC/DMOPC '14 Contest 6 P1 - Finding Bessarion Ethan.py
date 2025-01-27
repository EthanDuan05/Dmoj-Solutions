N = int(input())
station = []

for i in range(N):
    name = input()
    station.append(name)

loc = station.index('Bessarion')

if (station[loc - 1] == 'Bayview' and station[loc + 1] == 'Leslie') and 0 < loc < N-1:
    print('Y')
elif (station[loc - 1] == 'Leslie' and station[loc + 1] == 'Bayview') and 0 < loc < N-1:
    print('Y')
else:
    print('N')