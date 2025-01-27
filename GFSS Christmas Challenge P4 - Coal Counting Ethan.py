import sys
input = sys.stdin.readline

N, M = map(int, input().split())

naughtiness = list(map(int, input().split()))

year = list(map(int, input().split()))

naughtiness.sort()


def binary_search(arr, n):
    low = 0
    high = len(arr)-1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < n:
            low = mid + 1
        else:
            high = mid

    flag = True
    if arr[high] >= n:
        while flag:
            if arr[high-1] == arr[high] and high >= 1:
                high -= 1
                continue
            else:
                print(N - high)
                flag = False

    elif arr[low] >= n:
        while flag:
            if arr[low+1] == arr[low] and low <= N-1:
                low += 1
                continue
            else:
                print(N - low)
                flag = False


biggest = max(naughtiness)
smallest = min(naughtiness)

for i in year:
    if i > biggest:
        print(0)
    elif i == smallest:
        print(N)
    else:
        binary_search(naughtiness, i)