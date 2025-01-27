s = int(input())
k = int(input())
size = ((s+2)*3)+16
if size < k:
    print('Yes it fits!')
else:
    print("No, it's too small :(")