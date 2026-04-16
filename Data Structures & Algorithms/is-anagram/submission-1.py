class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False 
        x = {}
        for i in s:
            if i in x:
                x[i] +=1
            else :
                x[i] = 1 
        for i in t:
            if i not in x or x[i] == 0:
                return False 
            x[i] -=1
        return True