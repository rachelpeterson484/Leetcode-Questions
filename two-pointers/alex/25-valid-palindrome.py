class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join([c.lower() if c.isalpha() or c.isnumeric() else '' for c in s])
        return new_s == new_s[::-1]

        # alternative method, probably intended way as its under two pointers category
        # l, r = 0, len(new_s) - 1

        # while l < r:
        #    if new_s[l] != new_s[r]:
        #        return False
        #    l += 1
        #    r -= 1

        # return True
