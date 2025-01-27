N, M = map(int, input().split())
A = [0]*N
segtree = [[0, 0] for _ in range(2*N)]

debug = False

def build_segment_tree(A, N):
    for i in range(N):
        segtree[N + i] = [A[i], A[i]]

    for i in range(N - 1, 0, -1):
        a = max(segtree[2 * i][0], segtree[2 * i + 1][0])
        b = segtree[2 * i][1] + segtree[2 * i + 1][1]
        segtree[i] = [a, b]


def update(X, V):
    X += N
    segtree[X] = [V, V]

    while X > 1:
        X //= 2
        a = max(segtree[2 * X][0], segtree[2 * X + 1][0])
        b = segtree[2 * X][1] + segtree[2 * X + 1][1]
        segtree[X] = [a, b]


def range_query_max(start, end):
    start += N
    end += N

    MAX = -int(1e9)
    while start < end:
        if start & 1:
            MAX = max(MAX, segtree[start][0])
            start += 1

        if end & 1:
            end -= 1
            MAX = max(MAX, segtree[end][0])

        start //= 2
        end //= 2
    return MAX


def range_query_sum(start, end):
    start += N
    end += N
    result = 0

    while start < end:
        if start & 1:
            result += segtree[start][1]
            start += 1

        if end & 1:
            end -= 1
            result += segtree[end][1]

        start //= 2
        end //= 2
    return result


def bit_wise(a, b):
    return a ^ b

build_segment_tree(A, N)
last_ans = 0
# print(segtree)

for _ in range(M):
    S, a, b = input().split()
    a = int(a)
    b = int(b)
    a = bit_wise(a, last_ans)
    b = bit_wise(b, last_ans)
    if S == 'C':
        update(a-1, b)

    elif S == 'S':
        last_ans = range_query_sum(a-1, b-1+1)
        print(last_ans)

    elif S == 'M':
        last_ans = range_query_max(a-1, b-1+1)
        print(last_ans)

    if debug:
        print(segtree)

