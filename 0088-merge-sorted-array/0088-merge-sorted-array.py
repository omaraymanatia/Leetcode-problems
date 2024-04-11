class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j=0
        for i in range(n+m):
           if nums1[i]==0 and j<n:
            nums1[i]=nums2[j]
            j+=1
        nums1.sort()
