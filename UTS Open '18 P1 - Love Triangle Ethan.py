a, b = map(int, input().split())

A = a + b
B = abs(a-b)
C = a*b

print(max(A, B, C))