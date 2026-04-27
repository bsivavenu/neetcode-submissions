from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s).values()
        
        return max(f for f in counts if f % 2) - min(f for f in counts if not f % 2)