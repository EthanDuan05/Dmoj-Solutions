for _ in range(5):
    string = input()
    new = ''
    for kkk in string:
        if kkk.isalpha():
            N = ord(kkk) - ord('A')
            if N >= 13:
                new += chr(ord(kkk) - 13)
            elif N < 13:
                new += chr(ord(kkk) + 13)
        else:
            new += kkk

    print(new)