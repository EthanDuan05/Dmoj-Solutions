import sys

S = input()
T = input()

if len(S) > len(T):
    print('S')
elif len(S) < len(T):
    print('T')
else:
    for i in range(len(S)):
        if int(T[i]) > int(S[i]):
            print('T')
            sys.exit(0)
        elif int(T[i]) < int(S[i]):
            print('S')
            sys.exit(0)
    print('E')