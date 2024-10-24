from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        存在重复元素
        给定一个整数数组，判断是否存在重复元素。
        如果存在一值在数组中出现至少两次，函数返回 true 。
        如果数组中每个元素都不相同，则返回 false 。
        :param nums:
        :return:
        """
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
