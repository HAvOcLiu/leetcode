from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        生命游戏
        根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
        给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。
        每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。
        每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
            如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
            如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
            如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
            如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
        下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
        给你 m x n 网格面板 board 的当前状态，返回下一个状态。
        Do not return anything, modify board in-place instead.
        """
        # 0:dead
        # 1:live
        # 2:dead->live
        # 3:live->dead
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        value = board[i - 1][j - 1]
                        if value == 2:
                            value = 0
                        elif value == 3:
                            value = 1
                        count += value
                    value = board[i - 1][j]
                    if value == 2:
                        value = 0
                    elif value == 3:
                        value = 1
                    count += value
                    if j + 1 < n:
                        value = board[i - 1][j + 1]
                        if value == 2:
                            value = 0
                        elif value == 3:
                            value = 1
                        count += value
                if i + 1 < m:
                    if j - 1 >= 0:
                        value = board[i + 1][j - 1]
                        if value == 2:
                            value = 0
                        elif value == 3:
                            value = 1
                        count += value
                    value = board[i + 1][j]
                    if value == 2:
                        value = 0
                    elif value == 3:
                        value = 1
                    count += value
                    if j + 1 < n:
                        value = board[i + 1][j + 1]
                        if value == 2:
                            value = 0
                        elif value == 3:
                            value = 1
                        count += value
                if j - 1 >= 0:
                    value = board[i][j - 1]
                    if value == 2:
                        value = 0
                    elif value == 3:
                        value = 1
                    count += value
                if j + 1 < n:
                    value = board[i][j + 1]
                    if value == 2:
                        value = 0
                    elif value == 3:
                        value = 1
                    count += value
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 2
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
