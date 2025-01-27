T = int(input())

for _ in range(T):
    N = int(input())
    B = str(bin(N))[2:]
    B = B[::-1]
    print(int(B, 2))