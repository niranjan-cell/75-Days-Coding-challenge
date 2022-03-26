class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        for interval in intervals[1:]:
            if ans[-1][1]<interval[0]:
                ans.append(interval)
            elif ans[-1][1]<interval[1]:
                ans[-1][1]=interval[1]
        return ans
      """
      Time Complexity is O(n)
      """
