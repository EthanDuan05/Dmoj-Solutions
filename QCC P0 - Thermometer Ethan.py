T = int(input())

for _ in range(T):
    n = float(input())

    if n < 34:
        print('Too cold, please try again.')
    elif 34 <= n <= 35.5:
        print('Take a hot bath.')
    elif 35.5 < n <= 38:
        print('Rest if feeling unwell.')
    elif 38 < n <= 39:
        print('Take some medicine.')
    elif 39 < n <= 41:
        print('Take a cold bath and some medicine.')
    elif 41 < n <= 46.1:
        print('Go to the hospital.')
    elif 46.1 < n <= 50:
        print('Congrats, you have a new world record!')
    else:
        print('Too hot, please try again.')