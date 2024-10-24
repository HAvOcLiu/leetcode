from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        多数元素
        给定一个大小为 n 的数组，找到其中的多数元素。
        多数元素是指在数组中出现次数 大于  ⌊ n/2 ⌋  的元素。
        你可以假设数组是非空的，并且给定的数组总是存在多数元素。

        :param nums:
        :return:
        """
        count = 0  # 初始化选票数量为0
        candidate = nums[0]  # 初始化一个候选人，其实可以随机选
        for num in nums:
            if count == 0:
                # 选票没有了
                candidate = num  # 候选人下台，换一个新候选人上来
            if num == candidate:
                count += 1  # 数字和候选人一致，投赞成票，票数+1
            else:
                count -= 1  # 数字和候选人不一致，投反对票，票数-1
        return candidate
