class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        pre=[0]*n
        suff=[0]*n
        pre[0]=nums[0]
        suff[n-1]=nums[n-1]
        for i in range(1, n):
            pre[i]=pre[i-1]*nums[i]
        for i in range(n-2, -1, -1):
            suff[i]=suff[i+1]*nums[i]
        for i in range(n):
            if i==0:
                ans.append(suff[1])
            elif i==n-1:
                ans.append(pre[n-2])
            else:
                ans.append(pre[i-1]*suff[i+1])
        return ans
                