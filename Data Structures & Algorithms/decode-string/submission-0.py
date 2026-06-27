class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the multi-digit number (e.g., handling "12" instead of just "1")
                current_num = current_num * 10 + int(char)
                
            elif char == '[':
                # We are entering a new nested level.
                # Push what we have so far onto the stack to save it.
                stack.append((current_str, current_num))
                # Reset for the inner content
                current_str = ""
                current_num = 0
                
            elif char == ']':
                # We reached the end of the current encoding level.
                # Pop the outer string context and the multiplier k.
                prev_str, num = stack.pop()
                # Repeat the current string k times and append it to the previous string
                current_str = prev_str + (current_str * num)
                
            else:
                # It's a regular letter, just add it to our current working string
                current_str += char
                
        return current_str