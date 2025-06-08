class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            h, n = i, 0

            while h < len(haystack) \
                and n < len(needle) \
                and haystack[h] == needle[n]:
                h += 1
                n += 1

            if n == len(needle):
                return i

        return -1
