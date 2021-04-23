from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        被围绕的区域
        给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成。
        找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        if m < 2 or n < 2:
            return
        import collections

        def dfs(x, y):
            stack = collections.deque()
            stack.appendleft((x, y))
            board[x][y] = "P"

            while stack:
                current_x, current_y = stack[0]
                if 0 <= current_x - 1 < m and board[current_x - 1][current_y] == "O":
                    stack.appendleft((current_x - 1, current_y))
                    board[current_x - 1][current_y] = "P"
                    continue
                if 0 <= current_x + 1 < m and board[current_x + 1][current_y] == "O":
                    stack.appendleft((current_x + 1, current_y))
                    board[current_x + 1][current_y] = "P"
                    continue
                if 0 <= current_y - 1 < n and board[current_x][current_y - 1] == "O":
                    stack.appendleft((current_x, current_y - 1))
                    board[current_x][current_y - 1] = "P"
                    continue
                if 0 <= current_y + 1 < n and board[current_x][current_y + 1] == "O":
                    stack.appendleft((current_x, current_y + 1))
                    board[current_x][current_y + 1] = "P"
                    continue
                stack.popleft()

        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n - 1)

        for j in range(1, n - 1):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m - 1][j] == "O":
                dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "P":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

        print(board)
