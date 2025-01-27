n = int(input())

ans = []
for i in range(n):
    a, b = input().split()
    a = int(a)
    m = a-1
    L = b.strip(b[m])
    ans.append(L)

for i in range(len(ans)):
    print(str(i+1), ans[i])