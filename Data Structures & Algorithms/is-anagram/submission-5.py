class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # x = {}
        # for i in s:
        #     if i not in x:
        #         x[i] = 1
        #     else:
        #         x[i]+=1

        # x1 = {}
        # for i in t:
        #     if i not in x1:
        #         x1[i] = 1
        #     else:
        #         x1[i]+=1
        
        # return x == x1

        if len(s) != len(t):
            return False
            
        x, x1 = {}, {}
        for char in s:
            x[char] = x.get(char, 0) + 1
            
        for char in t:
            x1[char] = x1.get(char, 0) + 1
        
        return x == x1