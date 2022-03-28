class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r=0,len(matrix[0])
        u,d=0,len(matrix)
        ans=[]
        while l<r and u<d:
            # print()
            for i in range(l,r):
                # print(matrix[u][i])
                ans.append(matrix[u][i])
            u+=1
            for i in range(u,d):
                # print(matrix[i][r-1])
                ans.append(matrix[i][r-1])
            r-=1
            if not(l<r and u<d):
                break
            for i in range(r-1,l-1,-1):
                # print(matrix[d-1][i])
                ans.append(matrix[d-1][i])
                # print("here")
            d-=1
            for i in range(d-1,u-1,-1):
                # print(matrix[i][l])
                ans.append(matrix[i][l])
                
            l+=1
        return ans
