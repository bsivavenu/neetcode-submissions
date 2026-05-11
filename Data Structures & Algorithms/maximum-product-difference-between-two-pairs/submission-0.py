class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        m = sorted(nums)
        x = (m[-1]*m[-2])-(m[0]*m[1])
        return x