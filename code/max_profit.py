from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        买卖股票的最佳时机
        给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
        你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
        设计一个算法来计算你所能获取的最大利润。
        返回你可以从这笔交易中获取的最大利润。
        如果你不能获取任何利润，返回 0 。

        :param prices:
        :return:
        """
        min_price = prices[0]
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > min_price:
                result = max(prices[i] - min_price, result)
            elif prices[i] < min_price:
                min_price = prices[i]
        return result
