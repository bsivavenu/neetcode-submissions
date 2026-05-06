from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        x = Counter(nums)
        for i,j in x.items():
            if j %2 !=0:
                return False
        return True