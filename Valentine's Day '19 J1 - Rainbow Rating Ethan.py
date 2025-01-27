N = int(input())

for _ in range(N):
    num = int(input())
    if num < 1000:
        print('Newbie')
    elif 1000 <= num <= 1199:
        print('Amateur')
    elif 1200 <= num <= 1499:
        print('Expert')
    elif 1500 <= num <= 1799:
        print('Candidate Master')
    elif 1800 <= num <= 2199:
        print('Master')
    elif 2200 <= num <= 2999:
        print('Grandmaster')
    elif 3000 <= num <= 3999:
        print('Target')
    else:
        print('Rainbow Master')