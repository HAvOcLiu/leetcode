from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        四数相加II
        给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
        为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
        所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

        :param nums1:
        :param nums2:
        :param nums3:
        :param nums4:
        :return:
        """
        num1_num2_sum_dict = {}
        for num1 in nums1:
            for num2 in nums2:
                num1_num2_sum_dict[num1 + num2] = num1_num2_sum_dict.get(num1 + num2, 0) + 1

        result = 0
        for num3 in nums3:
            for num4 in nums4:
                if -num3 - num4 in num1_num2_sum_dict:
                    result += num1_num2_sum_dict[-num3 - num4]
        return result
