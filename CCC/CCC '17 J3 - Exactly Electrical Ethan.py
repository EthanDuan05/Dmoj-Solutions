a, b = map(int, input().split())
c, d = map(int, input().split())
t = int(input())

h_distance = abs(a - c)
v_distance = abs(b - d)

total = h_distance + v_distance

t -= total
if t >= 0 and t % 2 == 0:
    print('Y')
else:
    print('N')