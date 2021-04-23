from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        计算右侧小于当前元素的个数
        给定一个整数数组 nums，按要求返回一个新数组 counts。
        数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

        :param nums:
        :return:
        """

        unique_num_list = sorted(list(set(nums)))
        num_index_dict = {}
        for i, num in enumerate(unique_num_list, 1):
            num_index_dict[num] = i

        result_list = []
        count_list = [0] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            num_id = num_index_dict[num]
            position = num_id - 1
            result = 0
            while position > 0:
                result += count_list[position]
                low_bit = position & (-position)
                position -= low_bit
            result_list.append(result)
            position = num_id
            while position < len(count_list):
                count_list[position] += 1
                low_bit = position & (-position)
                position += low_bit
        result_list.reverse()
        return result_list
