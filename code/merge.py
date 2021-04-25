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

    def merge_sorted_array(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        合并两个有序数组
        给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
        初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
        你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        tail = m + n - 1
        while tail >= 0 and j >= 0:
            if i < 0 or nums2[j] >= nums1[i]:
                nums1[tail] = nums2[j]
                j -= 1
            else:
                nums1[tail] = nums1[i]
                i -= 1
            tail -= 1
