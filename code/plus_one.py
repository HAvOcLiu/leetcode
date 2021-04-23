from typing import List


class Solution:
    # 加一
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        digits[n] = digits[n] + 1
        while n >= 0:
            if digits[n] > 9:
                digits[n] = digits[n] - 10
                if n - 1 >= 0:
                    digits[n - 1] = digits[n - 1] + 1
                else:
                    digits = [1] + digits
                    return digits
            else:
                return digits
            n = n - 1
        return digits
