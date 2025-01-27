l = input()
h = ':-)'
s = ':-('
h_n = 0
s_n = 0

for i in range(len(l)-2):
    if l[i:i+3] == h:
        h_n += 1

for k in range(len(l)-2):
    if l[k:k+3] == s:
        s_n += 1

if h_n == 0 and s_n == 0:
    print('none')
elif h_n == s_n:
    print('unsure')
elif h_n > s_n:
    print('happy')
else:
    print('sad')