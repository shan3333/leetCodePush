class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j):
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!="O":
                return
            board[i][j] = "T"
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for x in range(len(board)):
            for y in range(len(board[0])):
                if (x==0 or y==0 or x==len(board)-1 or y==len(board[0])-1) and board[x][y]=="O":
                    dfs(x, y)

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]=="O":
                    board[x][y] = "X"
                elif board[x][y]=="T":
                    board[x][y] = "O"
                    
