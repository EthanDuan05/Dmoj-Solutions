n, k = map(int, input().split())

score = [ 0 for _ in range(n)]
worst_rank = [ -1 for _ in range(n)]

for _ in range(k):
    current_rank = []
    line = list(map(int, input().split()))

    for i in range(n):
        score[i] += line[i]

    for i in score:
        if i not in current_rank:
            current_rank.append(i)

    current_rank.sort(reverse=True)

    for i in range(n):
        rank = current_rank.index(score[i]) + 1
        if rank > worst_rank[i]:
            worst_rank[i] = rank

    # print(current_rank)

para = max(score)

for i in range(n):
    if score[i] == para:
        print('Yodeller ' + str(i+1) +  ' is the TopYodeller: score ' + str(score[i]) + ', worst rank ' + str(worst_rank[i]))

