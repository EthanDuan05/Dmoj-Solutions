import sys
input = sys.stdin.readline

T = int(input())

def LCP(s, t):
    n = min(len(s), len(t))
    for i in range(n):
        if s[i:i+1] != t[i:i+1]:
            return i
    return n

for _ in range(T):
    S = input().strip()
    Suffix_Array = []
    for i in range(len(S)):
        Suffix_Array.append(S[i:len(S)])

    Suffix_Array.sort()

    Count = len(Suffix_Array[0]) + 1
    for i in range(1, len(S)):
        lcp = LCP(Suffix_Array[i], Suffix_Array[i - 1])
        Count = Count + len(Suffix_Array[i]) - lcp

    print(Count)