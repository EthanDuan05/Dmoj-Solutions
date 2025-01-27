for _ in range(5):
    day, month, year = map(int, input().split())
    if year < 1997:
        print('old enough')
    else:
        if year == 1997:
            if month < 10:
                print('old enough')
            else:
                if month == 10:
                    if day <= 27:
                        print('old enough')
                    else:
                        print('too young')
                else:
                    print('too young')
        else:
            print('too young')