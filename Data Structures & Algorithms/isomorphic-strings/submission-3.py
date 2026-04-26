class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if len(set(s))!=len(set(t)):
        #    return False

        # x = {}
        # for i,j in zip(s,t):
        #     if i not in x:
        #         x[i]=j
            
        #     elif x[i] != j:
        #         return False

        # return True
        # return list(map(s.find, s)) == list(map(t.find, t))
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        
    