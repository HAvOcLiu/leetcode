class Solution:
    # 阶乘后的零
    def trailingZeroes(self, n: int) -> int:
        num_five = 0
        num_two = 0

        i = n // 2
        while i != 0:
            num_two += i
            i = i // 2

        i = n // 5
        while i != 0:
            num_five += i
            i = i // 5

        return min(num_five, num_two)
