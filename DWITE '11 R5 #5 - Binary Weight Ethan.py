for _ in range(5):
    debug = False
    num = int(input())
    L = bin(num)
    L = L[2:]
    length = len(L)
    index = 0
    number = 0

    if debug:
        print(L)

    if L.count('1') == 1 and L.count('0') == length-1:
        L += '0'
        print(int(L, 2))

    else:
        if L.count('1') == len(L):
            L = '0' + L

        ind_1 = L.rfind('1')
        ind_0 = L.rfind('0', 0, ind_1)

        if ind_0 == -1:
            L = '0' + L

        if debug:
            print(ind_1)
            print(ind_0)

        for i in range(length - 2, -1, -1):
            if L[i] == '0' and L[i + 1] == '1':
                string = L[i:]

                if debug:
                    print(string)

                number = string.count('1')
                L = L[:i] + '1' + '0'*(len(string)-1)
                break

        if debug:
            print(L)

        L = L[:len(L)-number+1] + '1'*(number-1)

        if debug:
            print(L)

        print(int(L, 2))