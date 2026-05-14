class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Step 1: Count the total number of strings
        n = len(words)
        
        # If there is only one string, it's already "equal" to itself
        if n == 1:
            return True
        
        # Step 2: Count the frequency of every character across all strings
        char_counts = {}
        for word in words:
            for char in word:
                char_counts[char] = char_counts.get(char, 0) + 1
        
        # Step 3: Check if each character's total count is divisible by n
        for count in char_counts.values():
            if count % n != 0:
                return False
        
        return True