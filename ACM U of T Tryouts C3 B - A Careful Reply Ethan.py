N = int(input())

for _ in range(N):
    ans = ['<3']
    line = input()
    for i in range(len(line)-1):
        if line[i] == '<' and line[i+1] == '3':
            ans.append('<3')
    print(' '.join(ans))