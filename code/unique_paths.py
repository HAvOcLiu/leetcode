class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        不同路径
        一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
        问总共有多少条不同的路径？
        :param m:
        :param n:
        :return:
        """
        count_matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            count_matrix[i][n - 1] = 1  # 每行的最后一列赋值为1
        for j in range(n):
            count_matrix[m - 1][j] = 1  # 最后一行的每一列赋值为1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                count_matrix[i][j] = count_matrix[i + 1][j] + count_matrix[i][j + 1]
        return count_matrix[0][0]
