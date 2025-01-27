line = input()
up = 0
low = 0
for i in line:
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1

if up > low:
    print(line.upper())
elif low > up:
    print(line.lower())
else:
    print(line)