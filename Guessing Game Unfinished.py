import sys
import random
A = 1
B = 10**9
for _ in range(30):
    y = 0
    if random.choice([True, False]):
        y = A
    else:
        y = B
    print(y)
    sys.stdout.flush()

    distance = int(input().strip())

    if distance == 0:
        sys.exit(0)

    if distance == -1:
        sys.exit(0)

    if distance > 0:
        A_new = max(1, y - distance)
        B_new = min(10 ** 9, y + distance)

        if random.choice([True, False]):  # Assume a fair coin toss
            A, B = A_new, y
        else:
            A, B = y, B_new

