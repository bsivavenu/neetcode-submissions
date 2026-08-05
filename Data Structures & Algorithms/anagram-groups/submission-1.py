from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        groups = defaultdict(list)
        
        for i in strs:
            count = [0] * 26
            for char in i:
                count[ord(char) - ord('a')] += 1
            signature = tuple(count)
            
            groups[signature].append(i)
        return (list(groups.values()))