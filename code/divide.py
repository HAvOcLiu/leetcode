class Solution:
    # 两数相除
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend > 0 > divisor) or (dividend < 0 < divisor)
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        result = 0
        for i in range(31, -1, -1):
            # 如果被除数右移i位之后仍大于等于除数
            # 则商就加上2的i次幂
            # 被除数更新为原被除数减去(除数左移i位)的结果
            if (abs_dividend >> i) >= abs_divisor:
                result = result + (1 << i)
                abs_dividend = abs_dividend - (abs_divisor << i)

        if negative:
            result = -result

        return result if -0x80000000 <= result <= 0x7fffffff else 0x7fffffff
