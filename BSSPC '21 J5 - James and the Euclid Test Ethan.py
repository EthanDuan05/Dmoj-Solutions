import sys
input = sys.stdin.readline

L = []
prime = [True for _ in range(int(300000+2))]

def find_smallest_larger_element(arr, target):
    low, high = 0, len(arr) - 1
    result = None

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > target:
            result = arr[mid]
            high = mid - 1
        else:
            low = mid + 1

    return result

def sieve(N):
    p = 2
    while p*p <= N:
        if prime[p]:
            for i in range(p*p, N+1, p):
                prime[i] = False

        p += 1

    for p in range(2, N+1):
        if prime[p]:
            L.append(p)

sieve(210000+1)

T = int(input())

prime[1] = False

for _ in range(T):
    x, k = map(int, input().split())

    if prime[x]:
        x_ind = L.index(x)
        Total = 0
        while k > 0:
            k -= 1
            Total += L[x_ind]
            x_ind += 1

        print(L[x_ind+k-1], Total)

    else:
        x_ind = 0
        if x < 2:
            x_ind = 0
        else:
            x_ind = L.index(find_smallest_larger_element(L, x))

        Total = 0
        while k > 0:
            k -= 1
            Total += L[x_ind]
            x_ind += 1

        print(L[x_ind + k - 1], Total)
