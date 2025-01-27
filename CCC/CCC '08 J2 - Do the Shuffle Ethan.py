line = ['A', 'B', 'C', 'D', 'E']

while True:
    b = int(input())
    n = int(input())
    if b == 4 and n == 1:
        break
    else:
        for i in range(n):
            if b == 1:
                line = line[1:5]+line[:1]
            elif b == 2:
                line = line[4:]+line[0:4]
            elif b == 3:
                line = line[1:2]+line[0:1]+line[2:5]
answer = ''
for k in line:
    answer += k+' '
print(answer)