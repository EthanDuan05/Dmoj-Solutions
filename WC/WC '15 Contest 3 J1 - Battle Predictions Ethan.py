b_a, b_d = map(int, input().split())
s_a, s_d = map(int, input().split())

if b_a > s_d and b_d > s_a:
    print('Batman')
elif b_a < s_d and b_d < s_a:
    print('Superman')
else:
    print('Inconclusive')