import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
segtree = [[0, 0] for _ in range(2 * N)]

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

lastAns = 0
A = [0] * N  # Initial array with N zeroes
build_segment_tree(A, N)

for _ in range(Q):
    S, a, b = input().split()
    a = int(a)
    b = int(b)
    a = bit_wise(a, lastAns)
    b = bit_wise(b, lastAns)
    if S == 'C':
        update(a - 1, b)
    elif S == 'S':
        lastAns = range_query_sum(a - 1, b)
        print(lastAns)
    elif S == 'M':
        lastAns = range_query_max(a - 1, b)
        print(lastAns)
