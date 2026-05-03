from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        c = Counter(x for row in grid for x in row)
        return [next(i for i in c if c[i] == 2),
                next(i for i in range(1, len(c) + 2) if c[i] == 0)]