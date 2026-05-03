from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        return list(map(pattern.find, pattern)) == list(map(words.index, words))
