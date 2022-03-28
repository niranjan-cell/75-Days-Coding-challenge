class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        def helper(i,j,k):
            if k>=len(word):
                return True
            if i>=len(board) or j>=len(board[0]) or i<0 or j< 0 or board[i][j]!=word[k] or (i,j) in visited:
                return False
            visited.add((i,j))
            left=helper(i,j-1,k+1)
            right=helper(i,j+1,k+1)
            up=helper(i-1,j,k+1)
            down=helper(i+1,j,k+1)
            visited.remove((i,j))
            return left or right or up or down
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited=set()
                if board[i][j]==word[0] and helper(i,j,0):
                    return True
        return False
                    
