import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
segtree = [[0, 0] for _ in range(2*N)]

debug = False


def finding_gcd(a, b):
    if b > 0:
        return finding_gcd(b, a%b)
    else:
        return a


def build_segment_tree(A, N):
    for i in range(N):
        segtree[N + i] = [A[i], A[i]]

    for i in range(N - 1, 0, -1):
        a = min(segtree[2 * i][0], segtree[2 * i + 1][0])
        b = finding_gcd(segtree[2 * i][1], segtree[2 * i + 1][1])
        segtree[i] = [a, b]


def update(X, V):
    X += N
    segtree[X] = [V, V]

    while X > 1:
        X //= 2
        a = min(segtree[2 * X][0], segtree[2 * X + 1][0])
        b = finding_gcd(segtree[2 * X][1], segtree[2 * X + 1][1])
        segtree[X] = [a, b]


def range_query_min(start, end):
    start += N
    end += N

    MIN = int(1e9)
    while start < end:
        if start & 1:
            MIN = min(MIN, segtree[start][0])
            start += 1

        if end & 1:
            end -= 1
            MIN = min(MIN, segtree[end][0])

        start //= 2
        end //= 2
    return MIN


def range_query_gcd(start, end):
    start += N
    end += N

    GCD = segtree[start][1]
    while start < end:
        if start & 1:
            GCD = finding_gcd(GCD, segtree[start][1])
            start += 1

        if end & 1:
            end -= 1
            GCD = finding_gcd(GCD, segtree[end][1])

        start //= 2
        end //= 2
    return GCD


build_segment_tree(A, N)
print(segtree)

for _ in range(M):
    S, a, b = input().split()
    a = int(a)
    b = int(b)
    if S == 'C':
        update(a-1, b)

    if S == 'M':
        print(range_query_min(a-1, b-1+1))

    if S == 'G':
        print(range_query_gcd(a-1, b-1+1))

    if S == 'Q':
        cnt = 0
        G = range_query_gcd(a-1, b-1+1)
        for i in range(a+N-1, b+N-1+1):
            if segtree[i][1] == G:
                cnt += 1
        print(cnt)

    if debug:
        print(segtree)

