a, b, c = map(int, input().split())
L = [a, b, c]
L.sort()

diff_1 = L[1] - L[0]
diff_2 = L[2] - L[1]

# difference same
if diff_1 == diff_2:
    print(L[-1]+diff_1)
else:
    if diff_1 > diff_2:
        print(L[0]+diff_2)
    else:
        print(L[1] + diff_1)