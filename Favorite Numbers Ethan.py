N = int(input())
line = list(map(int, input().split()))
line.sort()

dic = {}
for i in line:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1


def binary_search(arr, n):
    low = 0
    high = len(arr)-1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < n:
            low = mid + 1
        else:
            high = mid

    if arr[high] >= n:
        return arr[high]

    elif arr[low] >= n:
        return arr[low]


Q = int(input())
for _ in range(Q):
    nums = int(input())
    ans = binary_search(line, nums)
    print(ans, dic[ans])