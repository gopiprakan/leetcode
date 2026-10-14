class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum >9*num: 
            return ""
        n,r=divmod(sum,9)
        return("9" * n+str(r)+"0" * num)[:num]