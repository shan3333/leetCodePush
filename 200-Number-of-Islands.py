class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        h = len(grid[0])
        v = len(grid)
        islands = 0

        def dfs(x, y):
            if x<0 or x>=v or y<0 or y>=h or grid[x][y] != '1':
                return
            grid[x][y] = \0\
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        for i in range(v):
            for j in range(h):
                if grid[i][j] == \1\:
                    islands += 1
                    dfs(i,j)
                
        return islands
                
