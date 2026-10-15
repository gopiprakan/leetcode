class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        t=0
        for i in range(len(nums)):
            s=set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                t+=len(s) ** 2
        return t