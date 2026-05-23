class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                skip_i = s[i+1 : j+1]
                skip_j = s[i : j]
                return skip_i == skip_i[::-1] or skip_j == skip_j[::-1]
            i +=1
            j -=1

        return True