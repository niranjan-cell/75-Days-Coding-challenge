class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(candidates)
        def helper(tm,start,target):
            if target==0:
                return ans.append(list(tm))
            if target<0:
                return 
            for i in range(start,n):
                tm.append(candidates[i])
                helper(tm,i,target-candidates[i])
                tm.pop()
        helper([],0,target)
        return ans
                
