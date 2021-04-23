from typing import List


class Solution:
    # 除自身以外数组的乘积
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 0:
            return []

        result = [1] * length
        for i in range(1, length):
            result[i] = result[i - 1] * nums[i - 1]

        t = 1
        for j in range(length - 2, -1, -1):
            t = t * nums[j + 1]
            result[j] = result[j] * t
        return result
