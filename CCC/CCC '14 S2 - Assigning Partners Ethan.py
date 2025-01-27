n = int(input())
dic_1 = {}
dic_2 = {}
line_1 = input().split()
line_2 = input().split()

for s in range(n):
    dic_1[line_1[s]] = line_2[s]
    dic_2[line_2[s]] = line_1[s]

ans = []
for s in dic_1:
    if s in dic_2:
        if dic_1.get(s) != dic_2.get(s):
            ans.append('False')
        elif dic_1.get(s) == dic_2.get(s):
            if s == dic_1.get(s):
                ans.append('False')
            else:
                ans.append('True')
    else:
        ans.append('True')

if 'False' in ans:
    print('bad')
else:
    print('good')
