class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            d=sum(int(d) for d in str(nums[i]))
            if d==i:
                return i
        return -1