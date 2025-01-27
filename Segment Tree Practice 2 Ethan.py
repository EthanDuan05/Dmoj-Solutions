import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
segtree = [(float('inf'), -1) for _ in range(2 * N)]


def build_segment_tree(A, N):
    for i in range(N):
        segtree[N + i] = A[i]

    for i in range(N - 1, 0, -1):
        segtree[i] = segtree[2 * i] + segtree[2 * i + 1]


def update(index, value):
    index += N
    segtree[index] = value

    while index > 1:
        index //= 2
        segtree[index] = segtree[2 * index] + segtree[2 * index + 1]


def range_query_sum(start, end):
    start += N
    end += N
    result = 0

    while start < end:
        if start & 1:
            result += segtree[start]
            start += 1

        if end & 1:
            end -= 1
            result += segtree[end]

        start //= 2
        end //= 2

    return result


build_segment_tree(A, N)

for _ in range(Q):
    query = input().split()
    if query[0] == 'S':
        l, r = int(query[1]) - 1, int(query[2]) - 1
        ans = range_query_sum(l, r + 1)
        print(ans)
    elif query[0] == 'U':
        i, x = int(query[1]) - 1, int(query[2])
        update(i, x)
