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
        unique_num_list = sorted(list(set(nums)))  # 把输入数组去重，然后升序排列
        num_index_dict = {}  # 数字和对应id的索引字典
        for i, num in enumerate(unique_num_list, 1):
            num_index_dict[num] = i  # 构建索引字典

        result_list = [0] * len(nums)  # 最终的计数结果
        count_list = [0] * (len(nums) + 1)  # 临时计数数组
        for i in range(len(nums) - 1, -1, -1):
            # 倒序遍历输入数组
            num = nums[i]  # 取当前位置的数字
            num_id = num_index_dict[num]  # 取数字的id
            position = num_id - 1  # 初始化位置为id-1
            result = 0  # 初始化当前计数结果为0
            while position > 0:
                # 遍历求和，计算计数
                result += count_list[position]
                low_bit = position & (-position)
                position -= low_bit
            result_list[i] = result
            position = num_id
            while position < len(count_list):
                # 遍历更新临时计数数组
                count_list[position] += 1
                low_bit = position & (-position)
                position += low_bit
        return result_list
