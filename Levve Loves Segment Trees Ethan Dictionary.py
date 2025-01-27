import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

segtree = {}

def update(X, V):
    X += N
    segtree[X] = [V, V]

    while X > 1:
        X //= 2
        left = segtree.get(2 * X, [0, 0])
        right = segtree.get(2 * X + 1, [0, 0])
        a = max(left[0], right[0])
        b = left[1] + right[1]
        segtree[X] = [a, b]

def range_query_max(start, end):
    start += N
    end += N
    MAX = -int(1e9)

    while start < end:
        if start & 1:
            MAX = max(MAX, segtree.get(start, [0, 0])[0])
            start += 1
        if end & 1:
            end -= 1
            MAX = max(MAX, segtree.get(end, [0, 0])[0])
        start //= 2
        end //= 2
    return MAX

def range_query_sum(start, end):
    start += N
    end += N
    result = 0

    while start < end:
        if start & 1:
            result += segtree.get(start, [0, 0])[1]
            start += 1
        if end & 1:
            end -= 1
            result += segtree.get(end, [0, 0])[1]
        start //= 2
        end //= 2
    return result

def bit_wise(a, b):
    return a ^ b

last_ans = 0

for _ in range(Q):
    S, a, b = input().split()
    a = int(a)
    b = int(b)
    a = bit_wise(a, last_ans)
    b = bit_wise(b, last_ans)
    if S == 'C':
        update(a - 1, b)
    elif S == 'S':
        last_ans = range_query_sum(a - 1, b)
        print(last_ans)
    elif S == 'M':
        last_ans = range_query_max(a - 1, b)
        print(last_ans)
