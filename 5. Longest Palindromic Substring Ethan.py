# Brute force solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        N = len(s)
        Max_len = 0
        ans = s[0]

        for i in range(N - 1):
            for j in range(i + 1, N):
                if j - i + 1 > Max_len and s[i:j + 1] == s[i:j + 1][::-1]:
                    Max_len = j - i + 1
                    ans = s[i:j + 1]

        return ans

# Expand from the center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1: right]

        M_S = s[0]

        for i in range(len(s) - 1):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(M_S):
                M_S = odd
            if len(even) > len(M_S):
                M_S = even

        return M_S


