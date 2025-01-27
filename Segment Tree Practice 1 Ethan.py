import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
segtree = [(float('inf'), -1) for _ in range(2 * N)]


def build_segment_tree(A, N):
    for i in range(N):
        segtree[N + i] = (A[i], i)

    for i in range(N - 1, 0, -1):
        segtree[i] = min(segtree[2 * i], segtree[2 * i + 1], key=lambda x: (x[0], x[1]))


def update(index, value):
    index += N
    segtree[index] = (value, index - N)

    while index > 1:
        index //= 2
        segtree[index] = min(segtree[2 * index], segtree[2 * index + 1], key=lambda x: (x[0], x[1]))


def range_query_min(start, end):
    start += N
    end += N
    result = (float('inf'), -1)

    while start < end:
        if start & 1:
            result = min(result, segtree[start], key=lambda x: (x[0], x[1]))
            start += 1

        if end & 1:
            end -= 1
            result = min(result, segtree[end], key=lambda x: (x[0], x[1]))

        start //= 2
        end //= 2

    return result


build_segment_tree(A, N)

for _ in range(Q):
    query = input().split()
    if query[0] == 'M':
        l, r = int(query[1]) - 1, int(query[2]) - 1
        min_value, min_index = range_query_min(l, r + 1)
        print(min_value, min_index + 1)
    elif query[0] == 'U':
        i, x = int(query[1]) - 1, int(query[2])
        update(i, x)
