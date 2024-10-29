class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque()
        direction = [(1,0),(-1,0),(0,-1),(0,1)]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]=="O" and (x==0 or y==0 or x==len(board)-1 or y==len(board[0])-1):
                    queue.append((x,y))
                    
        while queue:
            x, y = queue.pop()
            board[x][y] = "T"
            for xd, yd in direction:
                x_new, y_new = x+xd, y+yd
                if x_new>=0 and y_new>=0 and x_new<len(board) and y_new<len(board[0]) and board[x_new][y_new]=="O":
                    queue.append((x_new, y_new))
                        


        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]=="O":
                    board[x][y] = "X"
                elif board[x][y]=="T":
                    board[x][y] = "O"
                    
