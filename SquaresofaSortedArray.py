class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        negArr=[]
        j,i=0,0
        for num in nums:
            
            if num<0:
                negArr.append(abs(num))
                j+=1
            else:
                break
        negArr=negArr[::-1]
        n,m=len(negArr),len(nums)
        while i<n and j<m:
            if negArr[i]<nums[j]:
                ans.append(negArr[i])
                i+=1
            else:
                ans.append(nums[j])
                j+=1
        if j<m:
            ans=ans+nums[j:]
        if i<n:
            ans=ans+negArr[i:]
        return list(map(lambda x: x**2,ans))
        
        """
        Time complexity is O(n)
        Space Complexity is O(n)
        """
