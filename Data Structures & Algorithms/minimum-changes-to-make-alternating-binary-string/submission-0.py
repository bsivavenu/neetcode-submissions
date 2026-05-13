class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        # Count changes needed to match the "0101..." pattern
        res = sum(int(c) == i % 2 for i, c in enumerate(s))
        
        # The result is the minimum of matching pattern A or pattern B (n - res)
        return min(res, n - res)