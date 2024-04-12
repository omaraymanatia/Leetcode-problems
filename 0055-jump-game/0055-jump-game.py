class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        mx=0
        for i in range(n):
            if i > mx:
                return 0
            mx= max(mx, i+nums[i])
            if mx>=n-1:
                return 1
        return 0