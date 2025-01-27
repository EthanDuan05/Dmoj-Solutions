R = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
Line = input()
P = 'YES'
for i in Line:
    if i not in R:
        P = 'NO'
        break
print(P)