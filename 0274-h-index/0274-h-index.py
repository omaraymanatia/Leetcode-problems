class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        citations.sort(reverse=True)
        ans=0
        mn=10000
        cnt=0
        for i in range(n):
            mn=min(mn, citations[i])
            cnt+=1
            if mn>=cnt:
                ans=max(ans, cnt)
            else:
                break
        return ans