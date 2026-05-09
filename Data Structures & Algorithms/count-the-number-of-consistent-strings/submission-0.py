class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # x = [j for i in i for i in words if j in allowed ]
        x = []
        for i in words:
            for j in i:
                if j not in allowed:
                    break
            else:
                x.append(i)
        return len(x)