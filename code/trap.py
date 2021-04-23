from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        接雨水
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
        :param height:
        :return:
        """
        if len(height) < 3:
            return 0

        rain = 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    rain += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    rain += right_max - height[right]
                right -= 1

        return rain
