from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        乘积最大子数组
        给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
        :param nums:
        :return:
        """
        max_value = nums[0]
        min_value = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            tmp_max = max_value
            tmp_min = min_value  # 当前最大值和当前最小值要同时更新，这里临时保留一下
            max_value = max(tmp_max * nums[i], nums[i], tmp_min * nums[i])
            min_value = min(tmp_min * nums[i], nums[i], tmp_max * nums[i])
            result = max(max_value, result)
        return result

    def maxProduct_mysteirous(self, nums: List[int]) -> int:
        """
        没搞明白为什么这么乘一下就对了……
        :param nums:
        :return:
        """
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)
