from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        旋转数组
        给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = (nums[i] for i in range(-(k % len(nums)), len(nums) - k % len(nums)))

    def rotate_image(self, matrix: List[List[int]]) -> None:
        """
        旋转图像
        给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
        你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
        Do not return anything, modify matrix in-place instead.
        """
        # 装逼用
        # matrix[:] = map(list, zip(*matrix[::-1]))

        # 低调的
        n = len(matrix)

        # 转置 -90
        for i in range(n):
            for j in range(i + 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        # 水平翻转 +180， 总+90
        for i in range(n):
            matrix[i] = matrix[i][::-1]
