s, m, l = map(int, input().split())
s_p, m_p, l_p = map(float, input().split())

sum = s + m + l
limit = 0
total = 0

while sum > 0:
    if limit < 3:
        if s > 0:
            s -= 1
            limit += 1
            total += s_p
            sum -= 1
        elif s == 0:
            if m > 0:
                limit += 1
                m -= 1
                total += m_p
                sum -= 1
            elif m == 0:
                limit += 1
                total += l_p
                sum -= 1
    elif limit == 3:
        if l > 0:
            l -= 1
            sum -= 1
        elif l == 0:
            if m > 0:
                m -= 1
                sum -= 1
            elif m == 0:
                s -= 1
                sum -= 1
        limit = 0

print('%.2f'%(total))



