import sys

flag = True

Operator = ['+', '-']

while flag:
    N = input()

    if N == '0':
        flag = False
        sys.exit(0)

    if len(N) == 1:
        print(N)

    else:
        S = list(N.split())
        ANS = []

        ind = []
        for i in range(len(S)):
            if S[i] in Operator:
                ind.append(i)

        ind.reverse()

        SET = []
        state = True

        for i in ind:
            if state:
                SET.append([S[i+1], S[i+2], S[i]])
                S[i], S[i + 1], S[i + 2] = '*', '*', '*'
                state = False

            else:
                if S[i+1] != '*':
                    SET.append([S[i+1], '#', S[i]])
                    S[i], S[i + 1] = '*', '*'
                else:
                    SET.append(['#', S[-1], S[i]])
                    S[i], S[-1] = '*', '*'

            print(S)

        ANS = []

        SET.reverse()
        print(SET)
        print(S)

        start = True

        for i in SET:
            if start:
                for k in i:
                    ANS.append(k)
                start = False

            else:
                inde = ANS.index('#')
                i.reverse()
                for k in i:
                    ANS.insert(inde+1, k)
                ANS.remove('#')

        print(' '.join(ANS))

