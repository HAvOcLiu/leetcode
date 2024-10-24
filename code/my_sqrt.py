class Solution:
    # x的平方根
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 4:
            return 1
        y = x * 0.5
        while True:
            y_new = 0.5 * (y + x / y)
            if y - y_new < 1:
                break
            y = y_new
        return int(y_new)
