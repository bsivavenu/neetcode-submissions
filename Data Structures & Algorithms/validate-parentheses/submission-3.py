class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, 
                # otherwise assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the stack's top element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were properly matched
        return not stack