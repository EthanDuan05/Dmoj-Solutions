n = int(input())
i = int(input())
j = int(input())

diff_i = abs(n-(i**2))
diff_j = abs(n-(j**2))

if diff_i > diff_j:
    print(2)
elif diff_i < diff_j:
    print(1)