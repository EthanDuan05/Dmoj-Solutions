import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, S = map(int, input().split())
    sequence = [0]*N
    for i in range(N):
        sequence[i] += i+1

    initial_sum = sum(sequence)
    sum_two = initial_sum - S

    possible_pairs = []
    for i in range(N-1):
        for s in range(i+1, N):
            if sequence[i] + sequence[s] == sum_two:
                possible_pairs.append((sequence[i], sequence[s]))

    print(len(possible_pairs))
