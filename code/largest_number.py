from typing import List


class LargerNumKey(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        最大数
        给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
        :param nums:
        :return:
        """
        str_nums = list(map(str, nums))
        str_nums.sort(key=LargerNumKey)  # 拼在一起排序，妙啊！
        result = "".join(str_nums)
        if result[0] == "0":
            return "0"
        else:
            return result
