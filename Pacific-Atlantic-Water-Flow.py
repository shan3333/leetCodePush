class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights) # row
        n = len(heights[0]) # column

        pac = [[False for _ in range(n)] for _ in range(m)]
        atlan = [[False for _ in range(n)] for _ in range(m)]

        dirs = [[0,-1], [0,1], [-1,0], [1,0]]
        def get_neighbors(x, y):
            neighbors = []
            for dir_x, dir_y in dirs:
                if 0<=x+dir_x<m and 0<=y+dir_y<n:
                    neighbors.append([x+dir_x, y+dir_y])
            return neighbors

        def dfs(x, y, ocean):
            if ocean[x][y]:
                return
            ocean[x][y] = True
            for x_new, y_new in get_neighbors(x,y):
                if heights[x_new][y_new] >= heights[x][y]:
                    dfs(x_new, y_new, ocean)

        for x in range(m):
            dfs(x, 0, pac)
            dfs(x, n-1, atlan)
        
        for y in range(n):
            dfs(0, y, pac)
            dfs(m-1, y, atlan)

        res = []
        for x in range(m):
            for y in range(n):
                if pac[x][y] and atlan[x][y]:
                    res.append([x,y])
        return res