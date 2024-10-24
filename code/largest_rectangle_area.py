from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        柱状图中最大的矩形
        给定 n 个非负整数，用来表示柱状图中各个柱子的高度。
        每个柱子彼此相邻，且宽度为 1 。
        求在该柱状图中，能够勾勒出来的矩形的最大面积。
        :param heights:
        :return:
        """

        heights = [0] + heights + [0]
        result = 0
        stack = [0]
        for i in range(1, len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - 1 - stack[-1]
                # result = max(result, height * width)
                area = height * width
                if area > result:
                    result = area
            stack.append(i)
        return result
