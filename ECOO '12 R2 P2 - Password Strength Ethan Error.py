for _ in range(10):
    password = list(input())
    password.append('')

    length = len(password)
    category = 0
    Uppercase = 0
    Lowercase = 0
    Digits = 0
    Symbols = 0
    Middle_Digit_and_Symbols = 0

    Consecutive_Uppercase = []
    Consecutive_Lowercase = []
    Consecutive_Digits = []

    Current_Consecutive_Uppercase = 0
    Current_Consecutive_Lowercase = 0
    Current_Consecutive_Digits = 0
    Current_Sequential_Digits = 0
    Current_Sequential_Letters = 0

    Max_Sequential_Letters = 0
    Max_Sequential_Digits = 0

    for i in range(0, length-1):
        last_difference = 0
        if password[i].isalpha():
            if password[i].isupper():
                Uppercase += 1
                if password[i+1].isupper():
                    if Current_Consecutive_Uppercase == 0:
                        Current_Consecutive_Uppercase += 2
                    else:
                        Current_Consecutive_Uppercase += 1

                    if abs(ord(password[i + 1]) - ord(password[i])) == 1:
                        if last_difference == 0:
                            last_difference = ord(password[i + 1]) - ord(password[i])
                            Current_Sequential_Letters += 2
                            if Current_Sequential_Letters > Max_Sequential_Letters:
                                Max_Sequential_Letters = Current_Sequential_Letters

                        else:
                            if ord(password[i + 1]) - ord(password[i]) == last_difference:
                                Current_Sequential_Letters += 1

                            if Current_Sequential_Letters > Max_Sequential_Letters:
                                Max_Sequential_Letters = Current_Sequential_Letters

                    else:
                        Current_Sequential_Letters = 0
                        last_difference = 0

                else:
                    Consecutive_Uppercase.append(Current_Consecutive_Uppercase)
                    Current_Consecutive_Uppercase = 0
                    Current_Sequential_Letters = 0
            else:
                Lowercase += 1
                if password[i+1].islower():
                    if Current_Consecutive_Lowercase == 0:
                        Current_Consecutive_Lowercase += 2
                    else:
                        Current_Consecutive_Lowercase += 1

                    if abs(ord(password[i+1])-ord(password[i])) == 1:
                        if last_difference == 0:
                            last_difference = ord(password[i+1])-ord(password[i])
                            Current_Sequential_Letters += 2

                            if Current_Sequential_Letters > Max_Sequential_Letters:
                                Max_Sequential_Letters = Current_Sequential_Letters

                        else:
                            if ord(password[i+1])-ord(password[i]) == last_difference:
                                Current_Sequential_Letters += 1

                            if Current_Sequential_Letters > Max_Sequential_Letters:
                                Max_Sequential_Letters = Current_Sequential_Letters

                    else:
                        Current_Sequential_Letters = 0
                        last_difference = 0

                else:
                    Consecutive_Lowercase.append(Current_Consecutive_Lowercase)
                    Current_Consecutive_Lowercase = 0
                    Current_Sequential_Letters = 0

        elif password[i].isdigit():
            Digits += 1
            if i != length-2 and i != 0:
                Middle_Digit_and_Symbols += 1

            if password[i+1].isdigit():
                if Current_Consecutive_Digits == 0:
                    Current_Consecutive_Digits += 2

                else:
                    Current_Consecutive_Digits += 1

                if abs(int(password[i+1])-int(password[i])) == 1:
                    if last_difference == 0:
                        last_difference = ord(password[i + 1]) - ord(password[i])
                        Current_Sequential_Digits += 2

                        if Current_Sequential_Digits > Max_Sequential_Digits:
                            Max_Sequential_Digits = Current_Sequential_Digits

                    else:
                        if ord(password[i + 1]) - ord(password[i]) == last_difference:
                            Current_Sequential_Digits += 1

                            if Current_Sequential_Digits > Max_Sequential_Digits:
                                Max_Sequential_Digits = Current_Sequential_Digits

                        else:
                            Current_Sequential_Digits = 0
                else:
                    Current_Sequential_Digits = 0
                    last_difference = 0

            else:
                Consecutive_Digits.append(Current_Consecutive_Digits)
                Current_Consecutive_Digits = 0
                Current_Sequential_Digits = 0

        else:
            Symbols += 1
            if i != length-2 and i != 0:
                Middle_Digit_and_Symbols += 1

    if Uppercase > 0:
        category += 1

    if Lowercase > 0:
        category += 1

    if Digits > 0:
        category += 1

    if Symbols > 0:
        category += 1

    # debug = False
    debug = True
    '''
    print(length - 1)
    print(Uppercase)
    print(Lowercase)
    print(Digits)
    print(Symbols)
    print(Middle_Digit_and_Symbols)

    print(Consecutive_Uppercase)
    print(Consecutive_Lowercase)
    print(Consecutive_Digits)

    print(Max_Sequential_Letters)
    '''
    print(Max_Sequential_Digits)

    Total = 0
    Total += (length-1)*4

    if debug: print(Total)

    if length-1 >= 8 and category >= 3:
        Total += 2 + 2*category
    if debug: print(Total)

    if Uppercase > 0:
        Total += 2*(length-1-Uppercase)
    if debug: print(Total)

    if Lowercase > 0:
        Total += 2*(length-1-Lowercase)
    if debug: print(Total)

    if Digits < length-1:
        Total += 4*Digits
    if debug: print(Total)

    Total += 6*Symbols
    if debug: print(Total)

    Total += 2*Middle_Digit_and_Symbols
    if debug: print(Total)

    if Uppercase + Lowercase == length-1:
        Total -= Uppercase + Lowercase
    if debug: print(Total)

    if Digits == length-1:
        Total -= Digits
    if debug: print(Total)

    for i in Consecutive_Uppercase:
        if i != 0:
            Total -= 2 * (i - 1)
    if debug: print(Total)

    for i in Consecutive_Lowercase:
        if i != 0:
            Total -= 2*(i-1)
    if debug: print(Total)

    for i in Consecutive_Digits:
        if i != 0:
            Total -= 2*(i-1)
    if debug: print(Total)

    if Max_Sequential_Letters > 2:
        Total -= 3*(Max_Sequential_Letters-2)
    if debug: print(Total)

    if Max_Sequential_Digits > 2:
        Total -= 3*(Max_Sequential_Digits-2)
    if debug: print(Total)

    if Total > 100:
        Total = 100

    if Total < 0:
        Total = 0

    if 0 <= Total <= 20:
        print('Very Weak' + ' ' + '(' + 'score = ' + str(Total) + ')')
    elif 21 <= Total <= 40:
        print('Weak' + ' ' + '(' + 'score = ' + str(Total) + ')')
    elif 41 <= Total <= 60:
        print('Good'+' '+'('+'score = '+str(Total)+')')
    elif 61 <= Total <= 80:
        print('Strong' + ' ' + '(' + 'score = ' + str(Total) + ')')
    else:
        print('Very Strong' + ' ' + '(' + 'score = ' + str(Total) + ')')
