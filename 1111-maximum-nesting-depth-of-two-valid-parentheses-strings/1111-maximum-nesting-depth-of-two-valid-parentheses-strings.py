class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans =[0]*len(seq)
        d=0
        for i,ch in enumerate(seq):
            if ch =='(':
                d+=1
                ans[i]=d%2
            else:
                ans[i]=d%2
                d-=1
        return ans