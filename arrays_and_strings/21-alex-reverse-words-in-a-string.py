class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        start = -1

        # could obviously just use split() and reverse() and join() from python as well
        for i, c in enumerate(s):
            if start == -1 and c != " ":
                start = i
            if start != -1 and (c == " " or i == len(s) - 1):
                words.append((start, i + (1 if i == len(s) - 1 and s[i] != " " else 0)))
                start = -1

        words.reverse()

        result = ""
        for word in words:
            result += s[word[0]:word[1]] + " "

        return result[:-1]

