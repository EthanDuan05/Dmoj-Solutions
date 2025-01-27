line = input().split()
n = int(input())
code = map(int, input().split())
decode = ''

for i in code:
    decode += line[i]

print(decode)