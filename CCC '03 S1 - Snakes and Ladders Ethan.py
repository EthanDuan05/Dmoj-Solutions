Flag = True
Specials = {54: 19, 90: 48, 99: 97, 9: 34, 40: 64, 67: 86}

square = 1
ANS = []
while Flag:
    num = int(input())
    if num < 2 or num > 12:
        print('You Quit!')
        Flag = False

    else:
        if square + num > 100:
            continue
        else:
            if square + num == 100:
                print('You are now on square ' + str(100))
                print('You Win!')
                Flag = False
            else:
                square = square + num
                if square in Specials:
                    square = Specials[square]

                print('You are now on square ' + str(square))