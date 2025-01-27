from math import comb

def combinations(m, k):
    return comb(m-1, k-1)

m = int(input())  # The given last number
k = 4   # Total numbers to choose, including m
print(combinations(m, k))
