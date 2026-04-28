
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        
        for i in strs:
            a = ''.join(sorted(i))
            if a not in x:
                x[a] = []
            x[a].append(i)

        return list(x.values())