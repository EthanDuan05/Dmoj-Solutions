n = int(input())
line = list(map(int, input().split()))

array = [0 for _ in range(50)]

for i in range(n):
    array[line[i]-1] += line[i]

ans = max(array)

print(array.index(ans)+1)