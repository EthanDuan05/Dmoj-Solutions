for _ in range(5):
    num = int(input())
    b_num = list(bin(num))
    b_num.pop(0)
    b_num.pop(0)
    s = len(b_num)
    for i in range(s-1, 0, -1):
        if b_num[i] == '0' and b_num[i+1] == '1':
            b_num[i], b_num[i+1] = b_num[i+1], b_num[i]
            break
