import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))

stored_value = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(0, N):
    stored_value[i][0] = 0
    stored_value[i][1] = 0


def finding_diff_sum(P, L):
    if L <= 1:
        return 0

    if stored_value[P][L] != -1:
        return stored_value[P][L]

    value = finding_diff_sum(P+1, L-2) + abs(line[P] - line[P+L-1])
    stored_value[P][L] = value
    return value


ans = [0]
for i in range(2, N + 1):
    min_stage = 1000000000000
    for k in range(0, N + 1 - i):
        stage = finding_diff_sum(k, i)
        if stage == 0:
            min_stage = 0
            break
        min_stage = min(stage, min_stage)
    ans.append(min_stage)

print(' '.join(map(str, ans)))