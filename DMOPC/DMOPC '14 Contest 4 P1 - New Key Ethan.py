new_dic = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

line = list(input())

ans = []
for i in line:
    ind = new_dic.index(i)
    new_ind = ind + 9
    ans.append(new_dic[new_ind])

print(''.join(ans))