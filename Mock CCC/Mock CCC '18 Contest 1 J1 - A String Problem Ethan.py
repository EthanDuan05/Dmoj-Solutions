N = int(input())

flag = True
while flag:
    N += 1
    if '0' not in str(N):
        print(N)
        flag = False