class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        mn_val=prices[0]
        for i in prices:
            ans=max(ans,i-mn_val)
            mn_val=min(mn_val,i)
        return ans
      """
      Space Complexity is O(1)
      Time Complexity is O(n)
      """
      
#ob = Solution()
#result=ob.maxProfit([7,1,5,3,6,4])
#print(result)
