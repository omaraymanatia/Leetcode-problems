class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        l = [[] for _ in range(numRows)]
        cnt=0
        f=1
        if numRows==1:
            f=cnt=0
        for i in range(n):
            l[cnt].append(i)
            cnt+=f
            if cnt==numRows:
                cnt-=2
                f=-1
            if cnt==-1:
                cnt+=2
                f=1
        print(l)
        ans=''
        for i in range(numRows):
            for j in l[i]:
                ans+=s[j]
        return ans
                