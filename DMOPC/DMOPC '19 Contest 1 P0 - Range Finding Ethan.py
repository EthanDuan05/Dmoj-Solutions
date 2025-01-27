N = int(input())

line = list(map(int, input().split()))

a = max(line)
b = min(line)

print(a - b)