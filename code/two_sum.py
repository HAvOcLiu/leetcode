from typing import List


class Solution:
    # 两数之和
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_dict = {}
        result = []
        for i in range(len(nums)):
            if target - nums[i] in num_index_dict.keys():
                index = num_index_dict.get(target - nums[i])
                if index != i:
                    result.append(index)
                    result.append(i)
                    return result
            num_index_dict[nums[i]] = i
