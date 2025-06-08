class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        numeral_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        i = 0
        while i < len(s):
            if s[i] == "I" and i+1 < len(s) and s[i+1] in {"V", "X"}:
                result += numeral_values[s[i+1]] - 1
                i += 2
            elif s[i] == "X" and i+1 < len(s) and s[i+1] in {"L", "C"}:
                result += numeral_values[s[i+1]] - 10
                i += 2
            elif s[i] == "C" and i+1 < len(s) and s[i+1] in {"D", "M"}:
                result += numeral_values[s[i+1]] - 100
                i += 2
            else:
                result += numeral_values[s[i]]
                i += 1

        return result

