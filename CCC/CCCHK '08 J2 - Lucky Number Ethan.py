N = int(input())

for _ in range(N):
    nums = input()
    while len(nums) > 1:
        ans = 0
        for i in nums:
            ans += int(i)
        nums = str(ans)

    print(nums)