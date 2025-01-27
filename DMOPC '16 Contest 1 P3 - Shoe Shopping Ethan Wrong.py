N = int(input())
Shoes = list(map(int, input().split()))

def compare(a, b):
    if a <= b:
        return a
    else:
        return b

def Calculate_2(a , b):
    T = a + b
    T2 = T - min(a, b) * 0.5
    return T2

def Calculate_3(a, b, c):
    T = a + b + c

    # two pair
    T2_1 = T - min(a, b) * 0.5

    T2_2 = T - min(b, c) * 0.5

    # three pair
    T3 = T - min(a, b, c)

    T2 = compare(T2_1, T2_2)

    if T2 <= T3:
        return T2
    else:
        return T3

if N == 1:
    print(Shoes[0])
elif N <= 2:
    Total = sum(Shoes)
    Cheapest = min(Shoes)
    print(Total - Cheapest*0.5)
elif 2 < N <= 3:
    Total = sum(Shoes)

    # two pair
    Total2_1 = Total - min(Shoes[0], Shoes[1])*0.5

    Total2_2 = Total - min(Shoes[1], Shoes[2])*0.5

    # three pair
    Total3 = Total - min(Shoes)

    print(min(Total2_1, Total2_2, Total3))
else:
    Cost = 0
    while Shoes:
        if len(Shoes) >= 3:
            ans1 = Calculate_3(Shoes[0], Shoes[1], Shoes[2])

            ans2 = Calculate_2(Shoes[0], Shoes[1])

            if ans1 <= ans2:
                Cost += ans1
                Shoes.pop(0)
                Shoes.pop(0)
                Shoes.pop(0)

            else:
                Cost += ans2
                Shoes.pop(0)
                Shoes.pop(0)

        else:
            if len(Shoes) == 1:
                Cost += Shoes[0]
                Shoes.pop(0)
            else:
                ans = Calculate_2(Shoes[0], Shoes[1])
                Cost += ans
                Shoes.pop(0)
                Shoes.pop(0)

        print(Cost)

    print(Cost)

