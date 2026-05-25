from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = []
        for i,j in zip_longest(word1,word2,fillvalue=''):
            x.append(i)
            x.append(j)
        return ''.join(x)