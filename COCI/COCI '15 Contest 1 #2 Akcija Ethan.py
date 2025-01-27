N = int(input())

L = []
for _ in range(N):
    book = int(input())
    L.append(book)

L.sort()
L.reverse()

if N <= 3:
    print(sum(L))
else:
    price = 0
    if N % 3 != 0:
        quo = N // 3
        diff = N - quo * 3
        for _ in range(diff):
            p = L.pop(-1)
            price += p

    while L:
        a = L.pop(0)
        b = L.pop(0)
        c = L.pop(0)
        price += a + b

    print(price)
