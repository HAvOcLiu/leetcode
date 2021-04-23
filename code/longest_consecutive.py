from typing import List


class Solution:
    # 最长连续序列
    def longestConsecutive(self, nums: List[int]) -> int:
        result_length = 1
        nums_set = set(nums)
        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1
                result_length = max(result_length, current_length)
        return result_length
