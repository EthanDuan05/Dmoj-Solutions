import sys

num = int(input())

add = num - 45

if add % 45 == 0:
    if add == 0:
        print("Let's go Bob!")
        sys.exit(0)

    if add % 2 == 0:
        print("Let's go Bob!")
    else:
        print("Rip Bob!")
else:
    print("Rip Bob!")