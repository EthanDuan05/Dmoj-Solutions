for _ in range(5):
    T , C = map(int, input().split())
    sum = 0
    cnt = 0
    current_eat = 1
    while T > 0:
        if sum >= C:
            sum = 0
            current_eat *= 2
            T -= current_eat
        else:
            T -= current_eat
            sum += current_eat
            cnt += 1

    print(cnt)