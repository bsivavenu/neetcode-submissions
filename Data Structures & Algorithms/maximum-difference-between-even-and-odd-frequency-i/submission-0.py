from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
    
        counts = Counter(s).values()
        odds = [f for f in counts if f % 2 != 0]
        evens = [f for f in counts if f % 2 == 0]
        return max(odds) - min(evens)
        