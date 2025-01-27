L = ['001', '002', '003', '004', '005', '006', '007', '008', '009']
cnt = 0
line = input().split('.')
for i in line:
    if i in L:
        cnt += 1

print(line)