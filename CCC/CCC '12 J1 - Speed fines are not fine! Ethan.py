k = int(input())
x = int(input())
if x <= k:
    print('Congratulations, you are within the speed limit!')
if x in range(k+1, k+21):
    print('You are speeding and your fine is $100.')
if x in range(k+21, k+31):
    print('You are speeding and your fine is $270.')
if x in range(k+31, k+1000):
    print('You are speeding and your fine is $500.')
