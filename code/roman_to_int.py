class Solution:
    # 罗马数字转整数
    def romanToInt(self, s: str) -> int:
        roman_int_dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        result = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] + s[i + 1] in roman_int_dict:
                result += roman_int_dict[s[i] + s[i + 1]]
                i += 2
            else:
                result += roman_int_dict[s[i]]
                i += 1
        return result
