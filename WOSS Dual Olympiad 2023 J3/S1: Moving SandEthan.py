import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

segtree = [0 for _ in range(2*N)]

def build_segment_tree(A, N):
    for i in range(N):
        segtree[N + i] = A[i]

    for i in range(N - 1, 0, -1):
        a = segtree[2 * i] + segtree[2 * i + 1]
        segtree[i] = a

def update(X, V):
    X += N
    segtree[X] = V

    while X > 1:
        X //= 2
        a = segtree[2 * X] + segtree[2 * X + 1]
        segtree[X] = a

def range_query_sum(start, end):
    start += N
    end += N

    Sum = 0
    if start == end:
        Sum = segtree[N + start]
    while start < end:
        if start & 1:
            Sum += segtree[start]
            start += 1

        if end & 1:
            end -= 1
            Sum += segtree[end]

        start //= 2
        end //= 2
    return Sum

build_segment_tree(A, N)

for _ in range(M):
    S, b, c = map(int, input().split())
    if S == 1:
        update(b-1-1, segtree[N+b-1-1] + c)
        update(b-1, segtree[N+b-1]-c)

    if S == 2:
        update(b, segtree[N+b] + c)
        update(b-1, segtree[N+b-1] - c)

    if S == 3:
        print(range_query_sum(b-1, c))