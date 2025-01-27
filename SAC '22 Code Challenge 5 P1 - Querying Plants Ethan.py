n = int(input())
c = int(input())
nums = input().split()

ans = ''
for i in range(len(nums)):
    A = int(nums[i]) + (2 * c)
    if i < len(nums)-1:
        ans += str(A) + ' '
    else:
        ans += str(A)

print(ans)