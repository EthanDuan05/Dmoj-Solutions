N = int(input())

number_of_a = 1
number_of_b = 0

for _ in range(N):
    new_a = number_of_b
    new_b = number_of_a + number_of_b
    number_of_a = new_a
    number_of_b = new_b



print(number_of_a, number_of_b)