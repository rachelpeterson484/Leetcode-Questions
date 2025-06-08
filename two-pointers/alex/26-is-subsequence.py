class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub = 0
        idx = 0

        while idx < len(t):
            if sub < len(s) and s[sub] == t[idx]:
                sub += 1
            idx += 1

        return sub == len(s)
