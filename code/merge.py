from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        合并区间
        以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
        请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x[0])
        result_list = []
        for interval in intervals:
            if not result_list or result_list[-1][1] < interval[0]:
                result_list.append(interval)
            else:
                result_list[-1][1] = max(result_list[-1][1], interval[1])
        return result_list
