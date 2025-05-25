class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights) # row
        n = len(heights[0]) # col
        res = []

        pac = [[False for _ in range(n)] for _ in range(m)]
        atlan = [[False for _ in range(n)] for _ in range(m)]

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] 
        def get_neighbors(x, y):
            neighbors = []
            for dir in dirs:
                new_x, new_y = x+dir[0], y+dir[1]
                if 0<=new_x<m and 0<=new_y<n:
                    neighbors.append([new_x,new_y])
            return neighbors
        
        def dfs(x, y, ocean):
            if ocean[x][y]:
                return
            ocean[x][y] = True
            neighbors = get_neighbors(x,y)
            for n_x, n_y in neighbors:
                if heights[n_x][n_y] >= heights[x][y]:
                    dfs(n_x, n_y, ocean)
            
        for x in range(m):
            dfs(x, 0, pac)
            dfs(x, n-1, atlan)

        for y in range(n):
            dfs(0, y, pac)
            dfs(m-1, y, atlan)
        
        for x in range(m):
            for y in range(n):
                if pac[x][y] and atlan[x][y]:
                    res.append([x,y])
        
        return res

