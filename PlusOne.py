class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        digits[-1]=digits[-1]+1
        ans=[0]+digits[:]
        for i in range(len(ans)-1,-1,-1):
            if ans[i]>9:
                ans[i]=0
                ans[i-1]+=1
            else:
                break
        # print(ans)
        if ans[0]!=0:
            return ans
        return ans[1::]
#ob=Solution()
#result=ob.plusOne([7,1,5,3,6,4])
#print(result)
