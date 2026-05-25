from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        # Find the length of the shorter string to avoid IndexErrors
        min_length = min(len(word1), len(word2))
        
        # 1. Alternate between both strings
        for i in range(min_length):
            result.append(word1[i])
            result.append(word2[i])
            
        # 2. Append the remaining characters from the longer string (if any)
        result.append(word1[min_length:])
        result.append(word2[min_length:])
        
        return ''.join(result)