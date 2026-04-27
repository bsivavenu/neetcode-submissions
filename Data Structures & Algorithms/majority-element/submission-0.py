from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        x = Counter(nums)
        for i,j in x.items():
            if j >=n:
                return i