a, b, c = map(int, input().split())

ans = max(b-a, c-b)-1
print(ans)