A_3 = int(input())
A_2 = int(input())
A_1 = int(input())
A_T = A_3*3+A_2*2+A_1*1
B_3 = int(input())
B_2 = int(input())
B_1 = int(input())
B_T = B_3*3+B_2*2+B_1*1
if A_T > B_T:
    print('A')
if B_T > A_T:
    print('B')
if A_T == B_T:
    print('T')