class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        # Count 1 for every word where ALL characters are in allowed
        return sum(all(char in allowed for char in word) for word in words)
