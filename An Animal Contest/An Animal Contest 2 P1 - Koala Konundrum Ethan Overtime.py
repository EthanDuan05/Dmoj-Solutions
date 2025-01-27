import sys
L = sys.stdin.readline

odd_letter = []
odd = 0

n = int(input())
s = list(input())

for i in s:
    m = s.count(i)
    if m % 2 != 0:
        if i not in odd_letter:
            odd_letter.append(i)
            odd += 1

print(max(1, odd))