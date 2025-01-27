n = int(input())
key = {}

for i in range(n):
    a, b = input().split()
    key[b] = a

line = input().split()
for s in range(len(line)):
    line[s] = line[s].strip('.')
    if line[s] in key:
        line[s] = key[line[s]]

cnt = 0
ans = ''
for i in line:
    if cnt < len(line)-1:
        ans += i+' '
        cnt += 1
    else:
        ans += i+'.'
print(ans)