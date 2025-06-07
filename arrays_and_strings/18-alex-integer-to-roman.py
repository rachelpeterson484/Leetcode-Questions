class Solution:
    def intToRoman(self, num: int) -> str:
        intToRoman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        integers = list(intToRoman.keys())
        integers.sort()

        result = ""
        while num > 0:
            intToUse = 0

            for integer in integers:
                if num >= integer:
                    intToUse = integer

            num -= intToUse
            result += intToRoman[intToUse]

        return result
