class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        螺旋矩阵
        给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
        :param matrix:
        :return:
        """
        up = 0
        down = len(matrix)
        left = 0
        right = len(matrix[0])
        result = []
        number = down * right
        while True:
            for j in range(left, right):
                result.append(matrix[up][j])
            if len(result) == number:
                break
            up += 1

            for i in range(up, down):
                result.append(matrix[i][right - 1])
            if len(result) == number:
                break
            right -= 1

            for j in range(right - 1, left - 1, -1):
                result.append(matrix[down - 1][j])
            if len(result) == number:
                break
            down -= 1

            for i in range(down - 1, up - 1, -1):
                result.append(matrix[i][left])
            if len(result) == number:
                break
            left += 1

        return result
