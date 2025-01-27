def find_possible_array(N, K):
    if K == 1:
        return list(range(N, 0, -1))

    if K == N:
        return [N] + list(range(1, N))

    a = list(range(N, N - K, -1)) + list(range(1, N - K + 1))
    return a


N, K = map(int, input().split())
print(find_possible_array(N, K))
