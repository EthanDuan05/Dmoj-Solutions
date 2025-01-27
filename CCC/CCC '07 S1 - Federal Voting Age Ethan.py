n = int(input())
answer = []

for i in range(n):
    y, m, d = map(int, input().split())
    if 2007 - y < 18:
        answer.append('No')
    elif 2007 - y > 18:
        answer.append('Yes')
    elif 2007 - y == 18:
        if 2 - m < 0:
            answer.append('No')
        elif 2 - m == 0 and 27 - d >= 0:
            answer.append('Yes')
        elif 2 - m == 1:
            answer.append('Yes')
        else:
            answer.append('No')

for i in answer:
    print(i)