N = int(input())
s = input()
numbers = list(map(int, s.split()))
print(*numbers, sep=" ")
for i in range(N+1):
    for j in range(N-1):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
            print(*numbers, sep=" ")