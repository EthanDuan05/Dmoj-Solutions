j = int(input())
a = int(input())

jerseys = ['']*j

for i in range(j):
    jeans = input()
    jerseys[i] += str(jeans)

cnt = 0
for s in range(a):
    order = input().split()
    if order[0] == 'S' and jerseys[int(order[1]) - 1] != '*':
        cnt += 1
        jerseys[int(order[1]) - 1] = '*'
    elif order[0] == 'M' and (jerseys[int(order[1]) - 1] == 'M' or jerseys[int(order[1]) - 1] == 'L'):
        cnt += 1
        jerseys[int(order[1]) - 1] = '*'
    elif order[0] == 'L' and jerseys[int(order[1]) - 1] == 'L':
        cnt += 1
        jerseys[int(order[1]) - 1] = '*'

print(cnt)