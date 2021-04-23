from typing import List


class Solution:
    # 单词搜索
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        m = len(board)
        n = len(board[0])
        len_word = len(word)
        visited = [[0] * n for x in range(m)]  # array shape: (m,n); 0: not visited, 1: visited

        for i in range(m):
            for j in range(n):
                step = 0
                if board[i][j] != word[step]:
                    continue

                stack = [(i, j, step)]  # (row, column, step)
                path = []  # (row, column, step) pairs to current value
                while stack:
                    current_x, current_y, step = stack.pop()
                    while path:
                        last_x_on_path, last_y_on_path, last_step_on_path = path[-1]
                        if last_step_on_path == step:  # synchronize path with current step
                            break
                        else:
                            path.pop()
                            visited[last_x_on_path][last_y_on_path] = 0

                    if board[current_x][current_y] == word[step]:
                        step += 1
                        if step == len_word:
                            return True
                        visited[current_x][current_y] = 1
                        path.append((current_x, current_y, step))
                        if current_x - 1 >= 0 and visited[current_x - 1][current_y] == 0:
                            stack.append((current_x - 1, current_y, step))
                        if current_x + 1 < m and visited[current_x + 1][current_y] == 0:
                            stack.append((current_x + 1, current_y, step))
                        if current_y - 1 >= 0 and visited[current_x][current_y - 1] == 0:
                            stack.append((current_x, current_y - 1, step))
                        if current_y + 1 < n and visited[current_x][current_y + 1] == 0:
                            stack.append((current_x, current_y + 1, step))
                while path:
                    last_x_on_path, last_y_on_path, _ = path.pop()  # stack is empty, so empty path
                    visited[last_x_on_path][last_y_on_path] = 0  # and clean visited array
        return False
