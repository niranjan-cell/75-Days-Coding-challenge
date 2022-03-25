from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict=Counter(nums)
        m=len(nums)//2
        for i,v in count_dict.items():
            if v>=m+1:
                return i
    """
    Time Complexity is O(n)
    Space Complexity is O(n)
    """
