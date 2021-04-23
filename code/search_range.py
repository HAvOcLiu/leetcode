from typing import List


class Solution:
    # 在排序数组中查找元素的第一个和最后一个位置
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        p = 0
        q = len(nums) - 1
        while p <= q:
            mid = (p + q) >> 1
            if target > nums[mid]:
                p = mid + 1
            elif target < nums[mid]:
                q = mid - 1
            else:
                p = mid - 1
                q = mid + 1
                while p >= 0 and nums[p] == target:
                    p = p - 1
                while q < len(nums) and nums[q] == target:
                    q = q + 1
                return [p + 1, q - 1]

        return [-1, -1]
