flag = True
ans = ['Ready']

while flag:
    k = input()
    if k == '  ':
        flag = False
    else:
        if 'b' and 'd' in k:
            ans.append('Mirrored pair')
        elif 'p' and 'q' in k:
            ans.append('Mirrored pair')
        else:
            ans.append('Ordinary pair')

for i in ans:
    print(i)