from typing import List


class Solution:
    # 缺失数字
    def missingNumber(self, nums: List[int]) -> int:
        total = ((0 + len(nums)) * (len(nums) + 1)) >> 1  # 等差数列求和
        return total - sum(nums)  # 减去数组的和得到缺失的数字
