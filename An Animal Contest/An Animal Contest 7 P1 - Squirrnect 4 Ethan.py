t = int(input())
answer = []
for i in range(t):
    w, h = input().split()
    w = int(w)
    h = int(h)
    if w == 1:
        answer.append('bad')
    elif w < 7 and h == 1:
        answer.append('bad')
    elif w < 4 and h < 4:
        answer.append('bad')
    else:
        answer.append('good')

for k in answer:
    print(k)