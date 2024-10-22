class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        h = len(grid[0])
        v = len(grid)
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(v):
            for j in range(h):
                if grid[i][j] == \1\:
                    islands += 1
                    queue = deque([(i,j)])
                    while queue:
                        x, y = queue.popleft()
                        if 0<=x<v and 0<=y<h and grid[x][y] == \1\:
                            grid[x][y] = \0\
                            for dx, dy in directions:
                                queue.append([x+dx, y+dy])

        return islands
                
