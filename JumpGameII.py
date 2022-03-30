class Solution:
    def jump(self, nums: List[int]) -> int:
        r,l=0,0
        potential=0
        ans=0
        while r<len(nums)-1:
            ans+=1
            for i in range(l,r+1):
                potential=max(potential,i+nums[i])
            l=r+1
            r=potential
        return ans
