from typing import List


class Solution:
    # 移动零
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = q = 0
        while p < len(nums) and q < len(nums):
            while p < len(nums) and nums[p] != 0:
                p = p + 1
            while q < len(nums) and nums[q] == 0:
                q = q + 1

            swap = False
            if p < len(nums) and p < q < len(nums):
                t = nums[p]
                nums[p] = nums[q]
                nums[q] = t
                swap = True
            if not swap:
                q = q + 1
