class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[10000]*n
        dp[0]=0
        ans=10000
        for i in range (n):
            for j in range (1, nums[i]+1):
                if i+j<n:
                    dp[i+j]=min(dp[i+j], dp[i]+1)
                else:
                    ans=min(ans, dp[i]+1)
        return min(ans, dp[n-1])