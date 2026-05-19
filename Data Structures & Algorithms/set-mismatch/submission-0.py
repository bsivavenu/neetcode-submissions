from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        duplicate = -1
        missing = -1
        
        # Loop from 1 to n (inclusive)
        for i in range(1, len(nums) + 1):
            if x[i] == 2:
                duplicate = i
            elif x[i] == 0:
                missing = i
                
        return [duplicate, missing]