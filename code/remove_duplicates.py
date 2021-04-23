from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        删除有序数组中的重复项
        给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
        不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

        :param nums:
        :return:
        """
        if not nums or len(nums) < 2:
            return len(nums)

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
