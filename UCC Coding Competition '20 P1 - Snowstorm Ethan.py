N = int(input())
line_1 = input()
line_2 = input()

possible_seats = 0
for i in range(N):
    if line_1[i] == '0' and line_2[i] == '0':
        possible_seats += 1

print(possible_seats)