class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        lookup=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                l,r=j+1,n-1
                while l<r:
                    total=nums[i]+nums[j]+nums[l]+nums[r]
                    if total<target:
                        l+=1
                    elif total>target:
                        r-=1
                    else:
                        t=(nums[i],nums[j],nums[l],nums[r])
                        if t not in lookup:
                            lookup.add(t)
                        while l<r and nums[l]==t[2]:l+=1
                        while l<r and nums[r]==t[3]:r-=1 
                while j+1<n and nums[j]==nums[j+1]:j+=1
            while i+1<n and nums[i]==nums[i+1]:i+=1
        return list(map(list,lookup))
