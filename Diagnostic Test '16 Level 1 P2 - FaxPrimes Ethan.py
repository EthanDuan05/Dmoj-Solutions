List = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

num = abs(int(input()))

Parameter_1 = False
Parameter_2 = False

for i in List:
    if num % i == 0:
        Parameter_1 = True
        break

length = len(str(num))

if length in List:
    Parameter_2 = True

if Parameter_1 and Parameter_2:
    print('true')
else:
    print('false')