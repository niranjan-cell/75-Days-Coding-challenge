from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indDict=defaultdict(list)
        for i in range(len(nums)):
            indDict[nums[i]].append(i)
        ans=[-1,-1]
        for i in range(len(nums)):
            start=indDict[nums[i]].pop()
            if indDict[nums[i]]==[]:
                del indDict[nums[i]]
            if ( target-nums[i] ) in indDict:
                end = indDict[target-nums[i]].pop()
                ans=[start,end]
                break
        return ans
      
      """
      The space and time complexity is O(n)
      """
    
#ob=Solution()
#result=twoSum([2,7,11,15],9)
#print(result)
