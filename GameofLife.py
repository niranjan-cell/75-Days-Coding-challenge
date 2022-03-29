class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        before | after  | val
           0   |    0   |   0 
           1   |    0   |   1
           0   |    1   |   2
           1   |    1   |   3
        """
        n=len(board)
        m=len(board[0])
        def helper(r, c):
            neg=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if i<0 or j<0 or i>=n or j>=m or (i==r and j==c):
                        continue
                    else:
                        if board[i][j] in [1,3]:
                            neg+=1
            return neg

        for i in range(n):
            for j in range(m):
                nig=helper(i,j)
                if board[i][j]:
                    if nig in [2,3]:
                        board[i][j]=3
                elif nig==3:
                    board[i][j]=2
                    
                
        for i in range(n):
            for j in range(m):
                if board[i][j]==1:
                    board[i][j]=0
                elif board[i][j] in [2,3]:
                    board[i][j]=1
        # for key,val in dic.items():
            # i,j=key[0],key[1]
            # board[i][j]=val
                    
