B = int(input())
Boxes = {}

for _ in range(B):
    l, w, h = map(int, input().split())
    L = [l, w, h]
    volume = l*w*h
    L.sort()
    Boxes[volume] = L

# print(Boxes)

I = int(input())
Items = []

for _ in range(I):
    l, w, h = map(int, input().split())
    L = [l, w, h]
    L.sort()
    volume = l*w*h

    min_volume = 10000000000000
    for i in Boxes:
        if volume <= i:
            if L[0] <= Boxes[i][0] and L[1] <= Boxes[i][1] and L[2] <= Boxes[i][2]:
                if i < min_volume:
                    min_volume = i

    if min_volume == 10000000000000:
        print('Item does not fit.')
    else:
        print(min_volume)


