from collections import Counter
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            triple = str(i) * 3
            if triple in num: 
                return triple
        return ""