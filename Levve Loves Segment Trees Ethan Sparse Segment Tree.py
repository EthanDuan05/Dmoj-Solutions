# sparse segment tree
import sys
input = sys.stdin.readline

tree = {}

def update(node, start, end, idx, value):
    # leaf node
    if start == end:
        tree[node] = (value, value)
        return

    mid = (start + end) // 2

    if idx <= mid:
        left_child = 2 * node
        if left_child not in tree:
            tree[left_child] = (0, 0)
        update(left_child, start, mid, idx, value)
    else:
        right_child = 2 * node + 1
        if right_child not in tree:
            tree[right_child] = (0, 0)
        update(right_child, mid + 1, end, idx, value)

    left_sum, left_max = tree.get(2 * node, (0, 0))
    right_sum, right_max = tree.get(2 * node + 1, (0, 0))
    tree[node] = (left_sum + right_sum, max(left_max, right_max))


def range_sum(node, start, end, l, r):
    if node not in tree or start > r or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node][0]

    mid = (start + end) // 2
    return range_sum(2 * node, start, mid, l, r) + range_sum(2 * node + 1, mid + 1, end, l, r)


def range_max(node, start, end, l, r):
    if node not in tree or start > r or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node][1]

    mid = (start + end) // 2
    return max(range_max(2 * node, start, mid, l, r), range_max(2 * node + 1, mid + 1, end, l, r))


def bit_wise(a, b):
    return a ^ b


N, Q = map(int, input().split())
last_ans = 0

for _ in range(Q):
    query = input().split()
    t = query[0]
    a = int(query[1])
    b = int(query[2])

    a = bit_wise(a, last_ans)
    b = bit_wise(b, last_ans)

    if t == 'C':
        update(1, 0, N - 1, a - 1, b)
    elif t == 'S':
        last_ans = range_sum(1, 0, N - 1, a - 1, b - 1)
        print(last_ans)
    elif t == 'M':
        last_ans = range_max(1, 0, N - 1, a - 1, b - 1)
        print(last_ans)
