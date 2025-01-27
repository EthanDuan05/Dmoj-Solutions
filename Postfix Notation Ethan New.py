line = input().split()
nums = []
ans = 0
for i in line:
    if i[0].isdigit():
        nums.append(float(i))
    else:
        nums_2 = nums.pop()
        nums_1 = nums.pop()
        if i == '*':
            ans = nums_1 * nums_2
        elif i == '/':
            ans = nums_1 / nums_2
        elif i == '+':
            ans = nums_1 + nums_2
        elif i == '-':
            ans = nums_1 - nums_2
        elif i == '%':
            ans = nums_1 % nums_2
        elif i == '^':
            ans = nums_1 ** nums_2
        nums.append(ans)

print(round(ans, 1))