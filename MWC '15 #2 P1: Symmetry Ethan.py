line = input()
length = len(line)

element = ['']*length

for i in range(len(line)):
    element[i] += (line[i])

first_line = ''
for i in range(length):
    first_line += element[i]*(i+1)

for i in range(length-2, -1, -1):
    first_line += element[i]*(i+1)

r = ((length**2)-1) // 2
ans = []
original_line = first_line
for i in range(1, r+1):
    new_line = list(original_line)
    new_line.pop(i)
    new_line.insert(i, line[0])
    new_line.pop(abs(i-length*length)-1)
    new_line.insert(abs(i-length*length)-1, line[0])
    new_line = ''.join(new_line)
    ans.append(new_line)
    original_line = new_line

ans_len = len(ans)
print(first_line)
for i in range(ans_len-1):
    print(ans[i])

for i in range(ans_len-1, -1, -1):
    print(ans[i])

print(first_line)