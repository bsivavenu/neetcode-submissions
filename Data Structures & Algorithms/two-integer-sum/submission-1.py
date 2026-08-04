class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i,j in enumerate(nums):
            y = target -j
            if y in x:
                return [x[y],i]
            x[j] = i