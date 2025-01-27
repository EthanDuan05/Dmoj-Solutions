import sys
input = sys.stdin.readline

N, M = map(int, input().split())

forbidden_flavors = [[] for i in range(N+1)]

for _ in range(M):
    f1, f2 = map(int, input().split())
    forbidden_flavors[f1].append(f2)

cnt = 0
for i in range(1, N+1):
    for s in range(1, N+1):
        for l in range(1, N+1):
            if (i < s) and (s < l):
                if (s in forbidden_flavors[i]) or (l in forbidden_flavors[i]):
                    continue
                elif (i in forbidden_flavors[l]) or (s in forbidden_flavors[l]):
                    continue
                elif (i in forbidden_flavors[s]) or (l in forbidden_flavors[s]):
                    continue
                else:
                    cnt += 1

print(cnt)