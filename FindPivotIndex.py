class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        _totalsum=sum(nums)
        leftsum=0
        left_p=0
        n=len(nums)
        while left_p<n:
            if _totalsum - nums[left_p] == leftsum*2:
                return left_p
            leftsum+=nums[left_p]
            left_p+=1
        return -1
      """
      Time Complexity is O(n)
      """
