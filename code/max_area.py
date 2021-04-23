from typing import List


class Solution:
    # 盛最多水的容器
    def maxArea(self, height: List[int]) -> int:
        p = 0
        q = len(height) - 1
        area = 0
        while p < q:
            area = max((q - p) * min(height[p], height[q]), area)
            if height[p] > height[q]:
                q -= 1
            else:
                p += 1
        return area
