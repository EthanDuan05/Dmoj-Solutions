N = int(input())

for _ in range(N):
    num = int(input())
    ans = '{0:b}'.format(num)
    ans = ans.replace('1', 'dank ')
    ans = ans.replace('0', 'meme ')
    print(ans.strip(ans[-1]))