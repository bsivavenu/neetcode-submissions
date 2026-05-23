class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome_range(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                # Instead of copying substrings, we just check the remaining indices
                return is_palindrome_range(i + 1, j) or is_palindrome_range(i, j - 1)
            i += 1
            j -= 1

        return True