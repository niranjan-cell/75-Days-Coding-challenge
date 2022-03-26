class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        target=0
        s=set()
        n=len(nums)
        for i in range(n):
            newtar=target-nums[i]
            j=i+1
            k=n-1
            while j<k:
                if nums[j]+nums[k] <newtar:
                    j+=1
                elif nums[j]+nums[k]>newtar:
                    k-=1
                else:
                    t=(nums[i],nums[j],nums[k])
                    if t not in s:
                        s.add(t)
                    
                    while j<k and t[1]==nums[j]:j+=1
                    while j<k and t[2]==nums[k]:k-=1
            while i+1<n and nums[i+1]==nums[i]:i+=1
        return list(map(list,s))
