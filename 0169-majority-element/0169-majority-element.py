class Solution(object):
    def majorityElement(self, nums):
        ans=-1
        count=0
        for i in nums:
            if not count:
                ans=i
                count+=1
            elif ans==i:
                count+=1
            else:
                count-=1
        return ans
