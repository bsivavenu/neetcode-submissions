class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Step 1: Count the frequency of characters in our inventory
        chars_count = Counter(chars)
        total_length = 0
        
        # Step 2: Check each word
        for word in words:
            word_count = Counter(word)
            
            # Step 3: Compare character requirements
            is_good = True
            for char, count in word_count.items():
                if count > chars_count[char]:
                    is_good = False
                    break
            
            # Step 4: If valid, add the length
            if is_good:
                total_length += len(word)
                
        return total_length