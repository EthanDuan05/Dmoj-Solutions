n = int(input())
new = []
flag = True
while flag:
    frequency = [0]*10
    y = n+1
    year = list(str(y))

    for i in year:
        m = int(i)
        frequency[m] += 1

    cnt = 0
    cnt += frequency.count(1)
    if cnt == len(year):
        print(y)
        flag = False
    else:
        n = y
        continue