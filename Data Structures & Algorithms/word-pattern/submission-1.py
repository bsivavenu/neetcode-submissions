from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # s = (s.split())
        # if len(s) != len(pattern):
        #     return False
        # x = {}
        # used_words = set()
        # for i,j in zip(pattern,s):
        #     if i in x:
        #         if x[i] != j:
        #             return False
        #     else:
        #         if j in used_words:
        #             return True
        #         x[i] = j
        #         used_words.add(j)
        # return True

        words = s.split()
        return list(map(pattern.find, pattern)) == list(map(words.index, words))
