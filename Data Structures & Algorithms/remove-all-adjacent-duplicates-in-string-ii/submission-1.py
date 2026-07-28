class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Stack will store elements as [char, count]
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                # Increment the count of the consecutive character
                stack[-1][1] += 1
            else:
                # New character encountered, push to stack with count 1
                stack.append([char, 1])
            
            # If the count reaches k, remove it from the stack
            if stack[-1][1] == k:
                stack.pop()
                
        # Rebuild the final string from the remaining characters in the stack
        return "".join(char * count for char, count in stack)