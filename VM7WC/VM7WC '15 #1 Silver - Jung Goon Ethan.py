N = int(input())

for _ in range(N):
    T = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    for l in range(T+1):
        for j in range(T-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                cnt += 1
    print('Optimal train swapping takes', cnt, 'swaps.')

