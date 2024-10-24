from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        有序矩阵中第K小的元素
        给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
        请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。

        :param matrix:
        :param k:
        :return:
        """
        n = len(matrix)
        left = matrix[0][0]  # 矩阵的最小值
        right = matrix[-1][-1]  # 矩阵的最大值
        while left < right:
            # 二分查找
            mid = (left + right) // 2

            # 确定了mid之后，数一下小于等于mid的值的数量count
            # 如果count大于等于k，说明我们的mid比较大，缩小right到mid，重新查找
            # 反之则把left扩大到mid+1
            i = n - 1
            j = 0
            # 查找从矩阵的左下方开始，向右上方进行
            # 也可从右上方开始，向左下方进行
            # 总之，这条对角线把矩阵一分为二，对角线左上方的值都小于等于mid，对角线右下方的值都大于mid
            count = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    count = count + i + 1
                    j += 1
                else:
                    i -= 1
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left
