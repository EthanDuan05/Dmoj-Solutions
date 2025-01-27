w = int(input())
h = int(input())

first = []
for i in range(w):
    if i % 2 == 0:
        first.append(0)
    else:
        first.append(1)

ans = [first]
previous = first
ans_sub = []
for _ in range(h-1):
    for i in range(w):
        if previous[i] == 0:
            ans_sub.append(1)
        else:
            ans_sub.append(0)

    ans.append(ans_sub)
    previous = ans_sub
    ans_sub = []


for i in ans:
    print(''.join(map(str, i)))