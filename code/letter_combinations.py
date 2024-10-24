from typing import List


class Solution:
    # 电话号码的字母组合
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_char_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = num_char_dict[digits[0]]
        for num in digits[1:]:
            chars = num_char_dict[num]
            new_result = []
            for combination in result:
                for char in chars:
                    new_combination = combination + char
                    new_result.append(new_combination)
            result = new_result
        return result
