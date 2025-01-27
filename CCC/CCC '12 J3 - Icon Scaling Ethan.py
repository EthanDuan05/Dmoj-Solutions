k = int(input())

line_i = ['*x*',\
          ' xx',\
          '* *']
for i in range(3):
    for j in range(k):
        line_f = ''
        for a in range(3):
            line_f += line_i[i][a]*k
        print(line_f)