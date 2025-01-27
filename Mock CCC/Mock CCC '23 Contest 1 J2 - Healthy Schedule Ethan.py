sleep = int(input())
wake = int(input())

length = (24 - sleep) + (wake - 0)

if 20 <= sleep <= 23 and 6 <= wake <= 9:
    if 8 <= length <= 10:
        print('Healthy')
    else:
        print('Unhealthy')
else:
    print('Unhealthy')
