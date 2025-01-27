Specials = {54: 19, 90: 48, 99: 97, 9: 34, 40: 64, 67: 86}

Start = 1
while True:
    step = int(input())
    if step == 0:
        print("You Quit!")
        break
    else:
        if Start + step > 100:
            Start += 0
        else:
            Start += step

        if Start in Specials:
            Start = Specials[Start]

        print("You are now on square " + str(Start))

    if Start == 100:
        print("You Win!")
        break
