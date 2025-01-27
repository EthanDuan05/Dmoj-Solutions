Square = 1
while True:
    n = int(input())
    if n < 2 or n > 12:
        print("You Quit!")
        quit()
    if Square + n <= 100:
        Square = Square + n

        if Square == 9:
            Square = 34
        if Square == 40:
            Square = 64
        if Square == 67:
            Square = 86
        if Square == 54:
            Square = 19
        if Square == 90:
            Square = 48
        if Square == 99:
            Square = 77

    print("You are now on square " + str(Square))

    if Square == 100:
        print("You Win!")
        quit()