import sys
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LargeNumberKey(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def __init__(self):
        self._answer = float("inf")

    def _coin_change(self, coins: List[int], amount: int, coin_index: int, count: int):
        if amount == 0:
            self._answer = min(self._answer, count)
            return

        if coin_index == len(coins):
            return

        k = amount // coins[coin_index]
        while k >= 0 and k + count < self._answer:
            self._coin_change(coins, amount - k * coins[coin_index], coin_index + 1, count + k)
            k -= 1

    # 零钱兑换
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        self._coin_change(coins, amount, 0, 0)
        return self._answer if self._answer != float("inf") else -1

    def minCoins(self, coins, amount):
        # coins: 硬币的面值
        # amount:想换取的纸钞面值

        # table[i] 存储换取面值为i的纸币，需要用到的最少量的硬币数
        table = [0 for i in range(amount + 1)]

        # Base case
        table[0] = 0

        # 初始化
        for i in range(1, amount + 1):
            table[i] = sys.maxsize

            # 对于每一种价值i来计算，最少用多少硬币可以换取？
        for i in range(1, amount + 1):

            # Go through all coins smaller than i
            for j in range(len(coins)):
                if coins[j] <= i:
                    sub_res = table[i - coins[j]]
                    if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                        table[i] = sub_res + 1
        return table[amount]


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("-91283472332"))
