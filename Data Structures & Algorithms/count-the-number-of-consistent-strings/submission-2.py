class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0

        for i in words:
            is_consistent = True  
            for j in i:
                if j not in allowed:
                    is_consistent = False
            if is_consistent:
                count +=1
        return count
