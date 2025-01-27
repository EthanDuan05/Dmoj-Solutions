def removeDuplicates(nums):
        ans = []

        for i in range(len(nums)):
            n = nums[i]
            if n not in ans:
                ans.append(n)

        for i in range(len(ans)):
            nums[i] = ans[i]

        return len(ans)

print(removeDuplicates([1, 1, 2]))