class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            row=[0]*(i+1)
            row[-1],row[0]=1,1
            for j in range (1,i):
                prev=ans[-1]
                row[j]=prev[j-1]+prev[j]
            ans.append(row)
        return ans
      """
      Time complexity is O(n)
      """
