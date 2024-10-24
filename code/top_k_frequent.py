from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        前K个高频元素
        给定一个非空的整数数组，返回其中出现频率前k高的元素。
        :param nums:
        :param k:
        :return:
        """
        num_count_dict = {}
        for num in nums:
            count = num_count_dict.get(num, 0)
            num_count_dict[num] = count + 1
        count_list = []
        for num in num_count_dict:
            count_list.append(num_count_dict[num])
        count_list.sort(reverse=True)
        count_limit = count_list[k - 1]
        result = []
        for num in num_count_dict:
            if num_count_dict[num] >= count_limit:
                result.append(num)
        return result
