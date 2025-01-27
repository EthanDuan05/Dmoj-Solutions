L = {'MG': 'midget girls', 'MB': 'midget boys', 'JG': 'junior girls', 'JB': 'junior boys',
     'SG': 'senior girls', 'SB': 'senior boys'}

line = input()
if line in L:
    print(L.get(line))
elif line not in L:
    print('invalid code')
