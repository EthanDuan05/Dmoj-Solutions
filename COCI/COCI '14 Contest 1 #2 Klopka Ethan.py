N = int(input())

Min_x = 100
Min_y = 100
Max_x = 0
Max_y = 0

debug = False
for _ in range(N):
    x, y = map(int, input().split())
    if x > Max_x:
        Max_x = x

    if y > Max_y:
        Max_y = y

    if x < Min_x:
        Min_x = x

    if y < Min_y:
        Min_y = y

if debug:
    print(Min_x)
    print(Min_y)
    print(Max_x)
    print(Max_y)

final_difference_x = Max_x - Min_x
final_difference_y = Max_y - Min_y

ans = max(final_difference_y, final_difference_x)

print(ans**2)