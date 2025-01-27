nums = []
for i in range(9):
    n = int(input())
    nums.append(n)

total = sum(nums)
difference = total - 100

poss = []
for s in range(0, 9):
    for k in range(0, 9):
        if nums[s] + nums[k] == difference and nums[s] != nums[k]:
            poss.append(nums[s])
            poss.append(nums[k])

nums.remove(poss[0])
nums.remove(poss[1])

for i in nums:
    print(i)
