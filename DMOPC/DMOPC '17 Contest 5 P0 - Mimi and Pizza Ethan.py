B = int(input())
Y = int(input())
state = input()

if B < 2:
    print('NO PIZZA')
else:
    if state == 'Y':
        if B // 2 >= Y:
            if B // 5 >= Y:
                print('B')
            else:
                print('D')
        else:
            print('NO PIZZA')
    else:
        if B // 2 >= Y:
            if B // 5 >= Y:
                print('A')
            else:
                print('C')
        else:
            print('NO PIZZA')