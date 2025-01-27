import sys; sys.stdout.flush()

low = 1
mid = 1 * (10 ** 9)
high = 2 * (10 ** 9)

while True:
    mid = (low + high) // 2
    print(mid)
    state = input()
    if state == 'SINKS':
        low = mid
    elif state == 'FLOATS':
        high = mid
    else:
        break