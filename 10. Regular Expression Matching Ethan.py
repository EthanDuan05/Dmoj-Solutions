def isMatch(s: str, p: str):
    dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
    dp[0][0] = True

    for l in range(2, len(p)+1):
        if p[l-1] == '*':
            dp[0][l] = dp[0][l-2]

    for j in range(1, len(s)+1):
        for k in range(1, len(p)+1):
            if s[j-1] == p[k-1] or p[k-1] == '.':
                dp[j][k] = dp[j-1][k-1]
            elif p[k-1] == '*':
                dp[j][k] = dp[j][k-2]
                if p[k-2] == '.' or p[k-2] == s[j-1]:
                    dp[j][k] |= dp[j-1][k]

    return dp[len(s)][len(p)], dp

p1, p2 = isMatch("ab", ".*")
print(p1)

for i in p2:
    print(i)