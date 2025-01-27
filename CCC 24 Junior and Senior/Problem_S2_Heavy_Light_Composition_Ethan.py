N, T = map(int, input().split())

for _ in range(N):
    phrase = input()
    frequency = [0 for _ in range(26)]
    for i in phrase:
        frequency[ord(i) - ord('a')] += 1

    ans = []
    Flag = True
    Debug = False
    State = 0
    one = ord(phrase[0]) - ord('a')
    two = ord(phrase[1]) - ord('a')

    if frequency[one] > 1 and frequency[two] == 1:
        State = 1
    elif frequency[one] == 1 and frequency[two] > 1:
        State = 2
    else:
        Flag = False

    if State == 1:
        PreviousState = State
        if Debug:
            print('1')

        for s in range(T - 1):
            a = ord(phrase[s]) - ord('a')
            b = ord(phrase[s + 1]) - ord('a')

            if PreviousState == 1:
                if frequency[a] > 1 and frequency[b] == 1:
                    PreviousState = 2
                    continue
                else:
                    Flag = False

            elif PreviousState == 2:
                if frequency[a] == 1 and frequency[b] > 1:
                    PreviousState = 1
                    continue
                else:
                    Flag = False

            if not Flag:
                break

    elif State == 2:
        PreviousState = State
        if Debug:
            print('2')
            print(frequency)

        for s in range(T - 1):
            a = ord(phrase[s]) - ord('a')
            b = ord(phrase[s + 1]) - ord('a')

            if PreviousState == 2:
                if frequency[a] == 1 and frequency[b] > 1:
                    PreviousState = 1
                    continue
                else:
                    Flag = False
                    break

            elif PreviousState == 1:
                if frequency[a] > 1 and frequency[b] == 1:
                    PreviousState = 2
                    continue
                else:
                    Flag = False
                    break

            if not Flag:
                break

    if Flag:
        print('T')
        Flag = True
    else:
        print('F')
        Flag = True

