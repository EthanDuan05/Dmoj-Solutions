a, b, c = map(int, (input()).split())
if c == a + b:
    print(str(a)+'+'+str(b)+'='+str(c))
elif a == b + c:
    print(str(a)+'='+str(b)+'+'+str(c))
elif a == b - c:
    print(str(a)+'='+str(b)+'-'+str(c))
elif c == a - b:
    print(str(a)+'-'+str(b)+'='+str(c))
elif a == b * c:
    print(str(a)+'='+str(b)+'*'+str(c))
elif c == a * b:
    print(str(a)+'*'+str(b)+'='+str(c))
elif c == a / b:
    print(str(a)+'/'+str(b)+'='+str(c))
elif a == b / c:
    print(str(a)+'='+str(b)+'/'+str(c))