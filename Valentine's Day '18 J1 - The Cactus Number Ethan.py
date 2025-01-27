max_c = -1e9

N = int(input())

for _ in range(N):
    num = int(input())
    if num > max_c:
        max_c = num

if max_c > 1000:
    if max_c > 10000:
        print('Something is wrong with these cuteness values')
    else:
        print('Cuteness by definition is similarity to Cactus')
else:
    print('Cuteness by definition is similarity to Carol')