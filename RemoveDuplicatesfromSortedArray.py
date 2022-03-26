class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,0
        while i<len(nums):
            if nums[i]==nums[j]:
                i+=1
            else:
                j+=1
                nums[j]=nums[i]
        return j+1
      """
      Time Complexity O(n)
      Space Complexity is O(1)
      """
            
