class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a=0
        ad=0
        for c in s:
            if c=='(':
                a+=1
            else:
                if a>0:
                    a-=1
                else:
                    ad+=1
        return ad+a