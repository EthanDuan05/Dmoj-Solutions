A, B, C = map(int, input().split())
L = [A, B, C]
L.sort()

print(max(L[0] * L[1] * L[2], L[0] + L[1] + L[2],
          L[0] * L[1] + L[2], L[0] + L[1] * L[2],
          L[0] * (L[1] + L[2]), (L[0] + L[1]) * L[2]))