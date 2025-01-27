def firstMissingPositive(nums):
    start = 1
    nums.sort()
    for i in nums:
        if i < start:
            continue
        elif i == start:
            start += 1
        else:
            return start

    if nums[-1] <= 0:
        return 1
    else:
        return nums[-1] + 1

print(firstMissingPositive([7,8,9,11,12]))