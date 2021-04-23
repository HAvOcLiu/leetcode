from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
        :param nums:
        :return:
        """
        # 数组长度
        n = len(nums)

        # 把负数都搞成超出范围的值
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # 如果 num 在数组里，就把数组下标 num-1 位置的数弄成负的
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # 第i个位置的数是正的，说明i+1就是答案
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # 全都不缺的时候n+1就是答案
        return n + 1
