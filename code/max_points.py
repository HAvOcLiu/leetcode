from typing import List


class Solution:
    def _gcd(self, a: int, b: int) -> int:
        # 最大公约数
        while b != 0:
            t = a % b
            a = b
            b = t
        return a

    # 直线上最多的点数
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        num_points = len(points)
        if num_points < 3:
            return num_points

        result = 2
        for i in range(num_points):
            point_on_line = 0
            duplicated_point = 0
            slope_count_dict = {}
            for j in range(i + 1, num_points):
                x = points[j][0] - points[i][0]
                y = points[j][1] - points[i][1]
                if x == 0 and y == 0:
                    duplicated_point += 1
                    continue
                elif y == 0:
                    horizontal = True
                else:
                    horizontal = False

                if horizontal:
                    key = "any@" + str(points[i][1])
                else:
                    gcd = self._gcd(x, y)
                    x = x // gcd
                    y = y // gcd
                    key = str(x) + "@" + str(y)
                slope_count_dict[key] = slope_count_dict.get(key, 0) + 1
                point_on_line = max(point_on_line, slope_count_dict.get(key))
            result = max(result, point_on_line + duplicated_point + 1)
        return result
