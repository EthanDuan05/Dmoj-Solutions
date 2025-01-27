x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

a = (x1 - x2)**2 + (y1 - y2)**2
b = (x2 - x3)**2 + (y2 - y3)**2
c = (x3 - x1)**2 + (y3 - y1)**2

print(min(a, b, c))