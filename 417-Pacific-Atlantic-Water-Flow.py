class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        l_v = len(heights)
        l_h = len(heights[0])  
        p_visited = set()
        a_visited = set()
        directions = ((-1,0), (1, 0), (0, -1), (0, 1))
        def dfs(visited, i,j):
            visited.add((i,j))
            for di, dj in directions:
                new_i, new_j = i+di, j+dj
                if 0<=new_i<l_v and 0<=new_j<l_h and heights[new_i][new_j]>=heights[i][j] and (new_i, new_j) not in visited:
                    dfs(visited, new_i, new_j)
        
        for m in range(l_v):
            dfs(p_visited, m, 0)
            dfs(a_visited, m, l_h-1)
        
        for n in range(l_h):
            dfs(p_visited, 0, n)
            dfs(a_visited, l_v-1, n)

        return p_visited.intersection(a_visited)
                