from typing import List


class Solution:
    # 矩阵中的最长递增路径
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        拓扑排序法
        :param matrix: 待查矩阵
        :return: 最长递增路径的长度
        """
        if not matrix:
            return 0

        m = len(matrix)  # 行
        n = len(matrix[0])  # 列

        # step 1: 计算每个元素的出度
        out_degree = [[0] * n for i in range(m)]  # 保存矩阵中每个元素的出度
        leaves = []  # 保存一次遍历之后出度为0的点
        for i in range(0, m):
            for j in range(0, n):
                if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:  # 上
                    out_degree[i][j] += 1
                if i + 1 < m and matrix[i][j] < matrix[i + 1][j]:  # 下
                    out_degree[i][j] += 1
                if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:  # 左
                    out_degree[i][j] += 1
                if j + 1 < n and matrix[i][j] < matrix[i][j + 1]:  # 右
                    out_degree[i][j] += 1

                if out_degree[i][j] == 0:
                    # 上下左右四次机会，没加1，出度为0
                    # 这个点比周围点都大，它是末尾
                    leaves.append((i, j))

        # step 2: 从出度为0的元素开始，逐步移除
        # 从邻居中找一个比他小的点，把那个点的出度减1，逐渐向小的地方推进
        # 最后连接起来就是一个递减的序列，反向就是递增的
        height = 0
        while leaves:
            height += 1  # 实际上就是遍历了几批出度为0的节点，每批会让序列长度加1
            new_leaves = []
            for (x, y) in leaves:  # 逐个遍历出度为0的点
                if x - 1 >= 0 and matrix[x][y] > matrix[x - 1][y]:  # 上
                    out_degree[x - 1][y] = out_degree[x - 1][y] - 1
                    if out_degree[x - 1][y] == 0:
                        new_leaves.append((x - 1, y))
                if x + 1 < m and matrix[x][y] > matrix[x + 1][y]:  # 下
                    out_degree[x + 1][y] = out_degree[x + 1][y] - 1
                    if out_degree[x + 1][y] == 0:
                        new_leaves.append((x + 1, y))
                if y - 1 >= 0 and matrix[x][y] > matrix[x][y - 1]:  # 左
                    out_degree[x][y - 1] = out_degree[x][y - 1] - 1
                    if out_degree[x][y - 1] == 0:
                        new_leaves.append((x, y - 1))
                if y + 1 < n and matrix[x][y] > matrix[x][y + 1]:  # 右
                    out_degree[x][y + 1] = out_degree[x][y + 1] - 1
                    if out_degree[x][y + 1] == 0:
                        new_leaves.append((x, y + 1))
            leaves = new_leaves
        return height
