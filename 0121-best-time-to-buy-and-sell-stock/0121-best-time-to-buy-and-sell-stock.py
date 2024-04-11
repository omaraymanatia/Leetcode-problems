class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn=10000
        ans=0
        for i in prices:
            mn=min(mn, i)
            ans=max(ans, i-mn)
        return ans
