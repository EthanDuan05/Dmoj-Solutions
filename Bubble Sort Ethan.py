n = int(input())
line = input()
nums = list(map(int, line.split()))
print(*nums, sep=' ')
for i in range(n+1):
    for j in range(n-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            print(*nums, sep=' ')
