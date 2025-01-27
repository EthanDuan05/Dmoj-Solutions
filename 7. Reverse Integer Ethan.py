def reverse(x: int):
    x = str(x)
    symbol = ''
    if x[0] == '-':
        symbol = '-'
        x = x[1:]

    x = x[::-1]
    x = symbol + x
    if -(2**31) <= int(x) <= 2**31-1:
        return int(x)
    else:
        return 0

print(reverse(120))