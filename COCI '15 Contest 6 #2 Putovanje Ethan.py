N, C = map(int, input().split())

Line = list(map(int, input().split()))

T = []

for i in range(N):
    current_C = Line[i]
    t = 1
    ind = 0

    if current_C > C:
        T.append(0)
    else:
        while current_C <= C and (ind + 1) < N:
            ind += 1
            t += 1
            current_C += Line[ind]
            print(ind)

    T.append(t)

print(T)
print(max(T))