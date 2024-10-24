from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        颜色分类
        给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
        此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        q = len(nums) - 1
        i = 0
        while p < q and i <= q:
            if nums[i] == 0:
                nums[i] = nums[p]
                nums[p] = 0
                p += 1
            if nums[i] == 2:
                nums[i] = nums[q]
                nums[q] = 2
                q -= 1
                i -= 1
            i += 1
