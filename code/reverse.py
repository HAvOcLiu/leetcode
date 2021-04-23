class Solution:
    # 整数反转
    def reverse(self, x: int) -> int:
        num = abs(x)
        result = 0
        while num > 0:
            t = num % 10
            num = num // 10
            result = result * 10 + t

        if result <= (1 << 31) - 1:
            if x < 0:
                result *= -1
            return result
        return 0
