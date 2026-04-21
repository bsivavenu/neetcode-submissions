class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        x = []
        n = len(strs)
        j = len(strs[0])
        
        for j in range(len(strs[0])):
            char = strs[0][j]
            for i in range(1,n):
                if j == len(strs[i]) or strs[i][j]!= char:
                    return ''.join(x)
            x.append(char)


        return ''.join((x))
