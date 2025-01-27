N = int(input())

for _ in range(N):
    line = input()
    C = None
    M = None
    if 'C' in line:
        C = True

    if 'M' in line:
        M = True

    if C == True and M == True: print('NEGATIVE MARKS')
    elif C == True or M == True: print('FAIL')
    elif C is None and M is None: print('PASS')