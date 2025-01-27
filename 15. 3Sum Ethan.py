''' Brute Force Solution
def threeSum(nums):
    N = len(nums)
    repeated = []
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if nums[i] + nums[j] + nums[k] == 0:
                    pair = [nums[i], nums[j], nums[k]]
                    pair.sort()
                    if pair not in repeated:
                        repeated.append(pair)

    return repeated

print(threeSum([-1,0,1,2,-1,-4]))
'''

# Smart Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans = []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                SUM = nums[i] + nums[j] + nums[k]
                if SUM > 0:
                    k -= 1
                elif SUM < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return ans