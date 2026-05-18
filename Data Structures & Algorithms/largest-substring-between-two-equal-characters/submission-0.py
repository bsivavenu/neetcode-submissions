class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Dictionary to store the first occurrence index of each character
        first_seen = {}
        max_len = -1
        
        for index, char in enumerate(s):
            if char in first_seen:
                # If we've seen it before, calculate the distance between the indices
                # We subtract 1 because we want the characters *between* them
                current_len = index - first_seen[char] - 1
                max_len = max(max_len, current_len)
            else:
                # If it's the first time seeing the character, record its index
                first_seen[char] = index
                
        return max_len