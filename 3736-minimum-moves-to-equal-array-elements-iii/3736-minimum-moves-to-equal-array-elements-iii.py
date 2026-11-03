class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx=max(nums)
        r=0
        for x in nums:
            r += mx -x
        return r