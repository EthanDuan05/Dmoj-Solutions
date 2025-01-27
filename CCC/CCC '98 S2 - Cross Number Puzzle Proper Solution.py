def perfect(x):
    factor = []
    for i in range(1, (int(x/2) + 1)):
        if x % i == 0:
            factor.append(i)
    if sum(factor) == x:
        return True
    else:
        return False


def cube(x):
    l = []
    for i in list(str(x)):
        l.append(int(i) ** 3)
    if sum(l) == x:
        return True
    else:
        return False


ans_1 = []
for i in range(1000, 10000):
    if perfect(i):
        ans_1.append(str(i))

ans_2 = []
for i in range(100, 1000):
    if cube(i):
        ans_2.append(str(i))

print(' '.join(ans_1))
print(' '.join(ans_2))