class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        f=0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                f=0
                j += 1
            elif nums[i]==nums[i-1] and not f:
                nums[j]=nums[i]
                j+=1
                f=1
        return j