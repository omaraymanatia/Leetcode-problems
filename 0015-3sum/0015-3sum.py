class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=set()
        for i in range(n):
            l = i+1
            r = n-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum<0:
                    l+=1
                elif sum>0:
                    r-=1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l+=1
        return list(ans)