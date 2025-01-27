import sys
input = sys.stdin.readline

N = int(input())
# data = sorted(map(int, (input().split())))

print(" ".join(map(str, sorted(map(int, (input().split()))))))