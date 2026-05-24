class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w_ptr = 0  # Pointer for word
        a_ptr = 0  # Pointer for abbr
        
        while a_ptr < len(abbr) and w_ptr < len(word):
            # Case 1: We encounter a number
            if abbr[a_ptr].isdigit():
                # Check for invalid leading zero
                if abbr[a_ptr] == '0':
                    return False
                
                # Parse the full number (it could be more than 1 digit, like '12')
                num = 0
                while a_ptr < len(abbr) and abbr[a_ptr].isdigit():
                    num = num * 10 + int(abbr[a_ptr])
                    a_ptr += 1
                
                # Skip the word pointer ahead by that number
                w_ptr += num
                
            # Case 2: We encounter a letter
            else:
                if word[w_ptr] != abbr[a_ptr]:
                    return False
                w_ptr += 1
                a_ptr += 1
        
        # Both pointers must reach the exact end of their strings
        return w_ptr == len(word) and a_ptr == len(abbr)