from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        unpaired = set()
        for x in nums:
            if x in unpaired:
                unpaired.remove(x)
            else:
                unpaired.add(x)
        
        return len(unpaired) == 0