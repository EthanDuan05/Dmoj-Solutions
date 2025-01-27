N = int(input())
current_max = 0
L = input().split()
string = ''
s_to_replace = input()
S = len(s_to_replace)

for i in range(N):
        if current_max < len(L[i]) <= S:
                current_max = len(L[i])
                string = L[i]

print(string)