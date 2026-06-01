class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            
            # Count the occurrences of the current character
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character to the current write position
            chars[write] = char
            write += 1
            
            # If the character repeated, write the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
        return write