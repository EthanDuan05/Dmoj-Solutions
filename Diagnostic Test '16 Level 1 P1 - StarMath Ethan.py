a = int(input())
op = input()
b = int(input())

ans = 0
if op == '$':
    ans = (int(a**2 - b**2))
elif op == '@':
    ans = (b*a//(2*a-3))
elif op == '#':
    ans = ((a*b)*(b-14))

print('The equation ' + str(a) + ' ' + op + ' ' + str(b) + ' ' + 'is equal to ' + str(ans) + '.')
