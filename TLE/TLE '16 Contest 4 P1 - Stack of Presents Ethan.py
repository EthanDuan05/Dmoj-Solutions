N = int(input())

L = []
for _ in range(N):
    num = int(input())
    L.append(num)

L.sort()

cumulative = 0
stack = 0
for i in L:
    if i >= cumulative:
        cumulative += i
        stack += 1
print(stack)