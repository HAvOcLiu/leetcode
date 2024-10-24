class Solution:
    # 分数到小数
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        fraction = ""
        if numerator / denominator < 0:
            fraction = fraction + "-"

        dividend = abs(numerator)  # 被除数
        divisor = abs(denominator)  # 除数
        fraction += str(dividend // divisor)  # 商

        remainder = dividend % divisor  # 余数
        if remainder == 0:
            return fraction  # 余数为零，除尽

        fraction = fraction + "."
        remainder_position_dict = {}  # 记录余数和余数的位置
        while remainder != 0:
            if remainder in remainder_position_dict:
                position = remainder_position_dict.get(remainder)
                fraction = fraction[:position] + "(" + fraction[position:] + ")"  # 给循环部分套上括号
                break
            remainder_position_dict[remainder] = len(fraction)
            remainder *= 10  # 余数补0，再除
            fraction = fraction + str(remainder // divisor)
            remainder = remainder % divisor  # 再算余数

        return fraction
