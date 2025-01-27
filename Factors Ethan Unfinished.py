import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = b-a+1
Sum = n*(a+b)/2

cnt = 0

i = 1
while i*i <= Sum:
    if Sum % i == 0:
        cnt += 1
        if Sum // i != i:
            cnt += 1
    i += 1


print(cnt)