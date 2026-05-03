class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count all characters in the input text
        counts = Counter(text)
        
        # We only care about the characters that make up "balloon"
        # For 'l' and 'o', we divide by 2 because we need two of each
        return min(
            counts['b'], 
            counts['a'], 
            counts['l'] // 2, 
            counts['o'] // 2, 
            counts['n']
        )