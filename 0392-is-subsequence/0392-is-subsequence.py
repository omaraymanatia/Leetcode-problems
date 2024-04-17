class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        j=0
        for i in t:
            if j>=len(s):
                break
            if i==s[j]:
                j+=1
        if j==n:
            return True
        else:
            return False