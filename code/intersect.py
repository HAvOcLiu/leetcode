from typing import List


class Solution:
    # 求交集
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        number_count_dict = {}
        for num in nums1:
            if num in number_count_dict.keys():
                number_count_dict[num] = number_count_dict[num] + 1
            else:
                number_count_dict[num] = 1

        result = []
        for num in nums2:
            if num in number_count_dict.keys():
                result.append(num)
                number_count_dict[num] = number_count_dict[num] - 1
                if number_count_dict[num] <= 0:
                    number_count_dict.pop(num)

        return result
