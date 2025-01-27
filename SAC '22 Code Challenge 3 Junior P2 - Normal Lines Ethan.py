x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if x1 == x2:
    print('y-axis')
elif y1 == y2:
    print('x-axis')
else:
    print('neither')