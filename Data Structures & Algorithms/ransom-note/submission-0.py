from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return len(set(ransomNote)) == len(set(magazine))
        return not (Counter(ransomNote)) - (Counter(magazine))
        # counter = 0
        # for i in magazine:
        #     if i not in ransomNote:
        #         return False
        #     else:
        #         return True