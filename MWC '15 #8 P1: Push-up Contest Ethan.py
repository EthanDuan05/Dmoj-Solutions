n = int(input())
nums = []

for i in range(1, n+1):
    nums.append(i)

for _ in range(n-1):
    number = int(input())
    nums.remove(number)

for i in nums:
    print(i)