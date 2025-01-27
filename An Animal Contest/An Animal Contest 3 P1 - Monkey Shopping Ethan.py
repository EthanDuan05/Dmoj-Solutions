L = ''
a, b, c, d = map(int, input().split())
if a >= b and c >= d:
    L = 'Stay home'
elif a >= b and c < d:
    L = 'Go to the pharmacy'
elif a < b and c < d:
    L = 'Go to the department store'
elif a < b and c >= d:
    L = 'Go to the grocery store'
print(L)