from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        摆动排序 II
        给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
        你可以假设所有输入数组都可以得到满足题目要求的结果。
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums, reverse=True)
        j = 0
        for i in range(1, len(sorted_nums), 2):
            nums[i] = sorted_nums[j]
            j += 1
        for i in range(0, len(sorted_nums), 2):
            nums[i] = sorted_nums[j]
            j += 1
        print(nums)
