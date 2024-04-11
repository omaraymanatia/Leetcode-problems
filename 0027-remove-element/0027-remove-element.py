class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        j=n-1
        while i<=j:
            if nums[i]==val:
                nums[i], nums[j]=nums[j], nums[i]  # swap function
                j-=1
            else:
                i+=1
        return i
        
                
            