n = int(input())
k = int(input())

sum = n

for i in range(1, k+1):
    new_a = n*10**i
    sum += new_a

print(sum)