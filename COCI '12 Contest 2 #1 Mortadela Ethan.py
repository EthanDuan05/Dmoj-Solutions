a, b = map(int, input().split())
a = a / b
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    ans = x / y
    if ans < a:
        a = ans

print(round(a*1000, 2))