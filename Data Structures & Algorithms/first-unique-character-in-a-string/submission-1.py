from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            # If the first time we see s[i] is ALSO the last time we see it:
            if s.find(s[i]) == s.rfind(s[i]):
                return i
        return -1