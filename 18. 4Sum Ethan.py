def fourSum(nums, target):
    nums.sort()
    L = len(nums)

    ANS = set()
    for i in range(L):
        for j in range(i+1, L):
            k = j + 1
            l = L-1
            while k < l:
                a = nums[i]
                b = nums[j]
                c = nums[k]
                d = nums[l]
                if a + b + c + d == target:
                    ANS.add((a, b, c, d))
                    k += 1
                    l -= 1
                elif a + b + c + d < target:
                    k += 1
                else:
                    l -= 1

    return list(ANS)

'''
def fourSum(nums, target):
    nums.sort()
    s = set()
    output = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            k = j + 1
            l = len(nums) - 1
            while k < l:
                sum = nums[i] + nums[j] + nums[k] + nums[l]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k], nums[l]))
                    k += 1
                    l -= 1
                elif sum < target:
                    k += 1
                else:
                    l -= 1
    output = list(s)
    return output
'''

print(fourSum([1,0,-1,0,-2,2], 0))