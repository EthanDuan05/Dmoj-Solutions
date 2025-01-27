Factorial = {'1': 1, '2': 2, '3': 6,
             '4': 24, '5': 120, '6': 720,
             '7': 5040, '8': 40320, '9': 362880, '0': 1}
debug = False

flag = True
while flag:
    n = input()
    List = []
    List.append(n)
    if n == '0':
        flag = False
    else:
        flag_n = True
        while flag_n:
            sum = 0
            num = list(n)
            if debug:
                print(num)

            for i in num:
                sum += Factorial[i]

            if sum in List:
                List.append(sum)
                flag_n = False
            else:
                List.append(sum)
                n = str(sum)
                continue

        print(len(List))




