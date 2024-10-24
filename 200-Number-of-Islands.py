class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid[0])
        v = len(grid)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        islands = 0
        
        queue = deque()
        for i in range(v):
            for j in range(h):
                if grid[i][j] == \1\:
                    queue.append((i,j))
                    grid[i][j] = \0\
                    islands += 1

                while queue:
                    x,y = queue.popleft()
                    for dx, dy in directions:
                        x_new, y_new = x+dx, y+dy
                        if grid[x_new][y_new] == \1\:
                            queue.append((x_new, y_new))
                            grid[x_new][y_new] = \0\

        return islands