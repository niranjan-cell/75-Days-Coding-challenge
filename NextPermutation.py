class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        lastpeak=-1
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                lastpeak=i
        if lastpeak==-1:
            for i in range(n//2):
                nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
            return nums
        final=lastpeak
        for i in range(lastpeak,n):
            if nums[i]<nums[final] and nums[i]>nums[lastpeak-1]:
                final=i
        nums[lastpeak-1],nums[final]=nums[final],nums[lastpeak-1]
        nums[:]=nums[:lastpeak]+sorted(nums[lastpeak:])
        
