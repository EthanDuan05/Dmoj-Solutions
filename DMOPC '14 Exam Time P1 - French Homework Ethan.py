a = input()
b = input()

ans = ''
ans += a + '-tu' + ' '
if b[-1] == 'e':
    ans += 'la' + ' ' + b + ' ?'
elif b[-1] == 's':
    ans += 'les' + ' ' + b + ' ?'
else:
    ans += 'le' + ' ' + b + ' ?'

print(ans)