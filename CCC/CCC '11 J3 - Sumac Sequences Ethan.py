import sys
input = sys.stdin.readline

flag = True
L = []
n_1 = int(input())
n_2 = int(input())


while flag:
    diff = n_1 - n_2
    if diff <= n_2:
        L.append(n_1)
        n_1 = n_2
        n_2 = diff
    elif diff > n_2:
        L.append(n_1)
        L.append(n_2)
        L.append(diff)
        flag = False


print(len(L))