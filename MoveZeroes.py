class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                temp.append(nums[i])
        for i in range(len(temp)):
            nums[i]=temp[i]
        for j in range(len(temp),len(nums)):
            nums[j]=0
            
    """
    Time Complexity is O(n)
    Space Complexity is O(1)
    """
            
# ob=Solution()
# arr=[0,1,0,3,12]
# ob.moveZeroes(arr)
