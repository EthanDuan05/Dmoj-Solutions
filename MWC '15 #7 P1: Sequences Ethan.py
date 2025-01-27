N = int(input())
line = list(map(int, input().split()))

Zero_lock = False
common_difference = line[1] - line[0]
common_ratio = 0

if 0 in line:
    print('both')
    Zero_lock = True
else:
    common_ratio = line[1] / line[0]

lock_common_difference = True
lock_common_ratio = True
is_common_difference = True
is_common_ratio = True

previous = 0
for i in range(N):
    if i < N-1:
        if line[i+1] - line[i] == common_difference:
            if lock_common_difference:
                is_common_difference = True
        else:
            is_common_difference = False
            lock_common_difference = False

        if not Zero_lock:
            if line[i+1] / line[i] == common_ratio and line[i] != 0:
                if lock_common_ratio:
                    is_common_ratio = True
            else:
                is_common_ratio = False
                lock_common_ratio = False

if not Zero_lock:
    if is_common_difference and is_common_ratio:
        print('both')
    elif is_common_difference:
        print('arithmetic')
    elif is_common_ratio:
        print('geometric')
    else:
        print('random')