H = int(input())
A = int(input())
S = int(input())

gain = min(A, H)

if (0 + gain - S) >= 0:
    print(0 + gain - S)
else:
    print(0)