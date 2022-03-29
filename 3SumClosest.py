class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=nums[0]+nums[1]+nums[-1]
        nums.sort()
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                twosum=nums[i]+nums[l]+nums[r]
                if twosum==target:
                    return twosum
                elif twosum<target:
                    l+=1
                elif twosum>target:
                    r-=1
                if abs(ans-target)>abs(twosum-target):
                    ans=twosum
        return ans
