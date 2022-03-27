class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache={0:1}
        curr=0
        ans=0
        for i in range(len(nums)):
            curr+=nums[i]
            # if curr==k:
            #     ans+=1
            if curr-k in cache:
                ans+=cache[curr-k]
            if curr in cache:
                cache[curr]+=1
            else:
                cache[curr]=1
        return ans
