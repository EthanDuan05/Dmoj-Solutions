N, M = map(int, input().split())
A = []
segtree = [0 for _ in range(2*N)]
debug = False


def build_segment_tree(A, N):
    for i in range(N):
        segtree[N + i] = A[i]

    for i in range(N - 1, 0, -1):
        a = min(segtree[2 * i], segtree[2 * i + 1])
        segtree[i] = a


def update(X, V):
    X += N
    segtree[X] = V

    while X > 1:
        X //= 2
        a = min(segtree[2 * X], segtree[2 * X + 1])
        segtree[X] = a


def range_query_min(start, end):
    start += N
    end += N

    MIN = int(1e7)
    while start < end:
        if start & 1:
            MIN = min(MIN, segtree[start])
            start += 1

        if end & 1:
            end -= 1
            MIN = min(MIN, segtree[end])

        start //= 2
        end //= 2
    return MIN


for _ in range(N):
    num = int(input())
    A.append(num)

build_segment_tree(A, N)

if debug: print(segtree)

for _ in range(M):
    Op, a, b = input().split()
    a = int(a)
    b = int(b)
    if Op == 'M':
        update(a, b)
    elif Op == 'Q':
        print(range_query_min(a, b+1))