# too complex, bad solution
def myAtoi(s: str):
    ans = ''
    s = list(s)
    state = True
    appears_p = False
    appears_m = False
    digits_appear = False
    while s:
        a = s.pop(0)
        if a == ' ':
            if digits_appear or appears_m or appears_p:
                break
            else:
                continue
        else:
            if a == '-':
                if (appears_m == True) or (appears_p == True) or (digits_appear == True):
                    break
                state = False
                appears_m = True
            elif a == '+':
                if (appears_m == True) or (appears_p == True) or (digits_appear == True):
                    break
                state = True
                appears_m = True
            else:
                if a.isdigit():
                    digits_appear = True
                    if a == '0':
                        if digits_appear:
                            ans += a
                        else:
                            continue
                    else:
                        ans += a
                else:
                    break

    if ans == '':
        return 0

    if state:
        ans = int(ans)
    else:
        ans = int(ans) * -1

    if -2**31 <= ans <= 2**31-1:
        return ans
    else:
        if ans > 2**31-1:
            return 2**31-1
        else:
            return -2**31



print(myAtoi("   -042"))

