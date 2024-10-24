import math
import sys


class Solution:
    def numSquares(self, n: int) -> int:
        """
        完全平方数
        给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
        你需要让组成和的完全平方数的个数最少。
        给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
        完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
        例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

        :param n:
        :return:
        """
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0  # 表示n本身就是一个完全平方数的情况

        # 接下来依次计算dp数组的每一项
        # dp[i]表示n等于i时的答案，最终的答案存在dp[n]里面
        for i in range(1, n + 1):
            # 内层循环是对我们准备好的每一个完全平方数
            # 用i减去这个数，计算余下部分还需要几个完全平方数
            for num in square_nums:
                # 因为我们是用i-num的，所以要保证i大于等于num
                if i < num:
                    break
                dp[i] = min(dp[i], dp[i - num] + 1)  # 这里比较了不同的拆分方案
        return dp[-1]

    def numSquares_math(self, n: int) -> int:
        # 按照一些数学知识，可能的答案只能是1,2,3或4.
        # 首先看4的条件
        while (n & 3) == 0:
            n = n >> 2  # 如果n可以被4整除，就把n除以4
        if (n & 7) == 7:
            return 4  # 形如 4^k*(8*m+7) 的数字由4个数字的完全平方和表示
        # 这一步结束的时候，n的值可能变了
        # 但是因为我们是每次都除以4，4本身是一个完全平方数
        # 所以这个缩放不影响最终的结果

        # 4排除了，还有1,2和3可选
        # n 本身是一个完全平方数
        # 也就是1的条件
        root = int(math.sqrt(n))
        if n == root * root:
            return 1

        # 4和1相继排除了，还剩下2和3可选
        # 看2的条件
        # 这里没有什么简便的方法，就是遍历一下
        for i in range(1, root + 1):
            # i作为其中一个组成部分
            # 看剩下的部分是不是一个完全平方数
            remand = n - i * i
            remand_root = int(math.sqrt(remand))
            if remand == remand_root * remand_root:
                return 2

        # 4,1和2都排除了，只能是3
        return 3
