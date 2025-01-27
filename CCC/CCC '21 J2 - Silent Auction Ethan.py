n = int(input())
w = ""
h_b = 0
for i in range(n):
    k = input()
    b = int(input())
    if b > h_b:
        w = k
        h_b = b
print(w)