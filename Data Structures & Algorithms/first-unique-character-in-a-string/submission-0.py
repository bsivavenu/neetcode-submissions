from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = Counter(s)
        for i in range(len(s)):
            # If the frequency of the character at index i is 1, return the index
            if x[s[i]] == 1:
                return i
                
        # If no unique character is found, return -1
        return -1