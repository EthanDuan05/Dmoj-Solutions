for _ in range(10):
    T = int(input())
    L = set()
    for _ in range(T):
        Line = input()
        ans = ''
        state_at = False
        state_skip = False
        for i in Line:
            if i == '@':
                state_at = True
                state_skip = False

            if i == '.' and not state_at:
                continue
            elif i == '.' and state_at:
                if i.isalpha():
                    ans += i.lower()
                else:
                    ans += i

            if i == '+':
                state_skip = True

            if state_skip:
                continue
            else:
                if i.isalpha():
                    ans += i.lower()
                else:
                    ans += i

        L.add(ans)

    print(len(L))

