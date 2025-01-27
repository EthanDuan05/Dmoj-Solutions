S = input()

nums = []

for i in S:
    if i != 'x':
        nums.append(int(i))

nums.sort()

product = 1
for i in nums:
    product *= i

print('x'.join(map(str, nums)))
print(product)