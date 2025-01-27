n = int(input())
d_b = []
d_i = []
size_b = []
size_i = []

for i in range(n):
    line_b = list(map(int, input().split()))
    volume_b = 1
    for s in line_b:
        volume_b *= s
    size_b.append(volume_b)
    d_b.append(line_b)

m = int(input())

for i in range(m):
    line_i = list(map(int, input().split()))
    volume_i = 1
    for k in line_i:
        volume_i *= k
    size_i.append(volume_i)
    d_i.append(line_i)

size_b.sort()

for i in range(m):
    cnt = False
    ind = 0
    for j in range(n):
        if size_i[i] <= size_b[j]:
            d_b[j].sort()
            L = d_b[j]
            for s in d_i[i]:
                if s <= (L[0] and L[1] and L[2]):
                    cnt = True
                    ind = j
            break
    if cnt:
        print(size_b[ind])
    else:
        print('Item does not fit.')