from typing import List


class Solution:
    # 岛屿数量
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        row_count = len(grid)
        if row_count == 0:
            return 0
        column_count = len(grid[0])
        island_count = 0

        for r in range(row_count):
            for c in range(column_count):
                if grid[r][c] == '1':
                    island_count += 1
                    grid[r][c] = '0'
                    neighbours = deque()
                    neighbours.append((r, c))
                    while len(neighbours) > 0:
                        (x, y) = neighbours.popleft()
                        if x - 1 >= 0 and grid[x - 1][y] == '1':
                            neighbours.append((x - 1, y))
                            grid[x - 1][y] = '0'
                        if x + 1 < row_count and grid[x + 1][y] == '1':
                            neighbours.append((x + 1, y))
                            grid[x + 1][y] = '0'
                        if y - 1 >= 0 and grid[x][y - 1] == '1':
                            neighbours.append((x, y - 1))
                            grid[x][y - 1] = '0'
                        if y + 1 < column_count and grid[x][y + 1] == '1':
                            neighbours.append((x, y + 1))
                            grid[x][y + 1] = '0'

        return island_count