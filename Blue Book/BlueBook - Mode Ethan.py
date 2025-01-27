sequence = {}
while True:
    num = int(input())
    if num == -1:
        break
    else:
        if num not in sequence:
            sequence[num] = 1
        else:
            sequence[num] += 1

a = max(sequence.values())

for i in sequence:
    if sequence[i] == a:
        print(i)