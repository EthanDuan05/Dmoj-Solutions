n = int(input())
L = []
for i in range(n):
    nums = int(input())
    L.append(nums)

L = sorted(L)
for i in L:
    print(i)